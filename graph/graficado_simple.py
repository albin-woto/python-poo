# figure permite graficar
# output_file permite elegir el formato de salida html
# Muestra el gráfico donde le indique, generalmente el browser
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    # Indico archivo e inicializo gráfico
    output_file('graficado_simple.html')
    fig = figure()

    # Indico cantidad de valores
    total_vals = int(input('Cuantos valores quieres graficar?: '))
    x_vals = list(range(total_vals))
    y_vals = []

    # Indico el valor de y para x
    for x in x_vals:
        val = int(input(f'Valor y para {x}:'))
        y_vals.append(val)

    # Configuro el gráfico con sus valores de x e y, además de configurar ancho de línea
    fig.line(x_vals, y_vals, line_width=2)
    # Indico que me muestre el gráfico fig
    show(fig)