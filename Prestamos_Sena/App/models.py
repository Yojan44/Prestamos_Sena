from django.db import models

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Aprendiz(models.Model):
    aprendiz_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    tipo_documento = models.CharField(max_length=2)
    numero_documento = models.CharField(max_length=20)
    ficha_aprendiz = models.CharField(max_length=20)

    def __str__(self):
        return self.numero_documento + " - " + self.nombre

class Equipo(models.Model):
    equipo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.numero_serie + " - " + self.nombre

class Accesorio(models.Model):
    accesorio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.numero_serie + " - " + self.nombre

class Prestamo(models.Model):
    prestamo_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    aprendiz_id = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    accesorio_id = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    estado_prestamo = models.CharField(max_length=50)

    class Meta:
        db_table = "Prestamo"

class Devolucion(models.Model):
    devolucion_id = models.AutoField(primary_key=True)
    prestamo_id = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    equipo_devuelto_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    accesorio_devuelto_id = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField()

class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    accesorio_id = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    estado = models.CharField(max_length=50)

