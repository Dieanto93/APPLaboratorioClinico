from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Examen_disponible
from .forms import PacienteForm, SeleccionarExamenesForm, ResultadoExamenForm, Pedido_examen

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Administrativo').exists():
                return redirect('administrative_dashboard')
            elif user.groups.filter(name='Tecnico').exists():
                return redirect('technician_dashboard')
            else:
                return redirect('unknown_role_dashboard')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def administrative_dashboard(request):
    pacientes = Paciente.objects.all()
    return render(request, 'administrative_dashboard.html', {'pacientes': pacientes})

def technician_dashboard(request):
    # Obtener todos los pacientes de la base de datos
    pacientes = Paciente.objects.all()
    # Renderizar la plantilla y pasar los pacientes como contexto
    return render(request, 'technician_dashboard.html', {'pacientes': pacientes})

def unknown_role_dashboard(request):
    return render(request, 'unknown_role_dashboard.html')

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrative_dashboard')
    else:
        return redirect('administrative_dashboard')  # Redirigir a otra página

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('administrative_dashboard')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})


def eliminar_paciente(request, paciente_id):
    # Obtener el paciente por su ID
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        # Eliminar el paciente de la base de datos si se confirma la acción
        paciente.delete()
        # Redirigir al usuario de vuelta al dashboard administrativo
        return redirect('administrative_dashboard')
    # Si no es una solicitud POST, mostrar una página de confirmación
    return render(request, 'confirmar_eliminacion_paciente.html', {'paciente': paciente})

def agregar_examenes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    examenes_disponibles = Examen_disponible.objects.all()

    if request.method == 'POST':
        form = SeleccionarExamenesForm(request.POST, examenes=examenes_disponibles)
        if form.is_valid():
            examenes_seleccionados_ids = [int(id) for id, seleccionado in form.cleaned_data.items() if seleccionado]
            # Crear un nuevo pedido de examen para el paciente
            pedido_examen = Pedido_examen.objects.create(paciente=paciente)
            # Asociar los exámenes seleccionados al pedido de examen
            pedido_examen.examenes_disponibles.add(*examenes_seleccionados_ids)
            messages.success(request, '¡Exámenes agregados con éxito!')
            # Redirigir al dashboard administrativo
            return redirect('administrative_dashboard')
    else:
        form = SeleccionarExamenesForm(examenes=examenes_disponibles)

    return render(request, 'agregar_examenes_paciente.html', {'paciente': paciente, 'form': form})

def pedidos_pendientes(request):
    # Obtener los pedidos pendientes
    pedidos_pendientes = Pedido_examen.objects.filter(resultados__isnull=True)
    return render(request, 'pedidos_pendientes.html', {'pedidos_pendientes': pedidos_pendientes})

def mostrar_resultados_examenes(request):
    # Aquí puedes agregar la lógica para obtener los resultados de los exámenes
    # desde la base de datos o cualquier otra fuente de datos.
    # Por ahora, simplemente renderizaremos una plantilla de resultados vacía.
    return render(request, 'mostrar_resultados_examenes.html')

def ver_pedidos_pendientes(request):
    # Agrega la lógica necesaria para obtener los pedidos pendientes
    # desde la base de datos o cualquier otra fuente de datos.
    # Por ahora, simplemente renderizaremos una plantilla vacía.
    return render(request, 'ver_pedidos_pendientes.html')

def agregar_resultados_examenes(request):
    # Lógica para obtener los datos necesarios para el formulario de resultados de exámenes
    # Por ejemplo, puedes obtener la lista de pacientes con pedidos pendientes de exámenes
    # y los detalles de los exámenes solicitados para cada paciente.
    
    # Aquí iría tu lógica para obtener los datos necesarios
    # patients_with_pending_orders = ...

    # Luego, pasas los datos al template
    return render(request, 'agregar_resultados_examenes.html', {
        # Puedes pasar los datos necesarios al template como contexto
        # 'patients_with_pending_orders': patients_with_pending_orders,
    })

def ingresar_resultados_examenes(request, pedido_id):
    pedido = get_object_or_404(Pedido_examen, pk=pedido_id)
    
    if request.method == 'POST':
        form = ResultadoExamenForm(request.POST)
        if form.is_valid():
            resultado_examen = form.save(commit=False)
            resultado_examen.pedido = pedido
            resultado_examen.save()
            return redirect('detalle_pedido', pedido_id=pedido_id)  # Redirige a la página de detalles del pedido o donde desees
    else:
        form = ResultadoExamenForm()
    
    return render(request, 'ingresar_resultados.html', {'form': form, 'pedido': pedido})
