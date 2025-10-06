class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"Producto(id={self.id},nombre={self.nombre},precio={self.precio},cantidad={self.cantidad})"

    
class CrudProducto:
    def __init__(self):
        self.productos = []


    def create(self, id, nombre, precio, cantidad):
        producto = Producto(id, nombre, precio, cantidad)
        self.productos.append(producto)
        return producto
    
    def read(self, id):
        for producto in self.productos:
            if id == producto.id:
                return producto
        return None
    
    def readAll(self):
        return self.productos
    
    def update (self, id, nombre = None, precio = 0.0, cantidad = 0):
        for producto in self.productos:
            if producto.id == id:
                if nombre:
                    producto.nombre = nombre
                if precio != 0.0:
                    producto.precio = precio
                if cantidad != 0:
                    producto.cantidad = cantidad
                return producto
        return None
    
    def delete(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                return -1
        return 0
    
crudProducto = CrudProducto()

print("=== CREATE ===")
crudProducto.create(100, 'Camiseta', 5.0, 25)
crudProducto.create(101, 'Pantalon', 10.99, 30)
crudProducto.create(102, 'Abrigo', 25.5, 14)
crudProducto.create(103, 'Gorro', 3.99, 40)
print(crudProducto.readAll())

print("===READ===")
print(crudProducto.read(102))

print("===UPDATE===")
print(crudProducto.update(102, "Camiseta2", 0.0, 55))
print(crudProducto.read(102))

print("===DELETE===")
print(crudProducto.delete(102))
print(crudProducto.readAll())


            

            
