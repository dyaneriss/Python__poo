from persona import persona

juan = persona("Juan", "castellanos", 15)
juan.MostrarPersona()

leidy = persona("leidy", "Alvarez", 18)
leidy.MostrarPersona()

leidy.apellidos = "Perez"
leidy.mostrarPersona()

juan = leidy

juan.mostrarPersona()