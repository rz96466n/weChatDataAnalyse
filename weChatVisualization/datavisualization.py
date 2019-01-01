

def piechart(place,number):

    from pyecharts import Pie
    attr = place
    v1 = number
    pie = Pie("Friends Location")
    pie.add("Nan = not specific", attr, v1, is_label_show=True)
    return pie

def liquid_chart(name,number):
    from pyecharts import Liquid

    liquid = Liquid(name)
    liquid.add("",shape='circle',is_liquid_animation=True,is_liquid_outline_show=True,data=[number])

    return liquid
# value=[12,5,6,7]
# attr=['China','United States','Canada','Russia']
# piechart(attr,value)

def bar_chart(name,number):
    from pyecharts import Bar

    attr=name
    value=number
    bar=Bar(title ='Top 10 places \n of your frineds location')
    bar.add('Your Friends',attr,value,is_stack=True)
    bar.use_theme('westeros')
    bar.render(path='first.html')
    return bar
if __name__=='__main__':
    print('ok')
    name=['friends']
    number=[5]
    bar_chart(name,number).render(path='first.html')