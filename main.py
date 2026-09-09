from pyscript import display, document

def create_order(e):
    document.getElementById('result').innerHTML="  "
    prod1 = document.getElementById('item1')
    prod2 = document.getElementById('item2')
    prod3 = document.getElementById('item3')
    prod4 = document.getElementById('item4')
    prod5 = document.getElementById('item5')

    subtotal = float(prod1.value) * prod1.checked
    # subtotal = float(prod2.value) * prod2.checked
    # subtotal = float(prod3.value) * prod3.checked
    # subtotal = float(prod4.value) * prod4.checked
    # subtotal = float(prod5.value) * prod5.checked
    display(f'Your payment is {subtotal}', target='show')