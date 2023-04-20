import PySimpleGUI as sg
import qrcode

pepe = '123456'
img = qrcode.make("GRSTINJVGY2DKNJSGIYDINZUMY2GKNDFGQYTEMBUG42DSNJWGQ2TEMBVHE2GMNJVGIYDKNJVGAZDANDFGQ2TKNRUGU2TEMRQGRSTINJVGY2DKNJSGIYDIZJUGU2TMNBVGUZAU===")

sg.theme('DarkBrown')   # Add a touch of color
# All the stuff inside your window.

left_col = [[sg.Text('Save key from file', font = ("italic",25), text_color = "white")],
            [sg.Text(pad=(0,5))],
            [sg.Text('Issuer Name:', font = ("italic",18))], 
            [sg.InputText(key='-Issuer-', size=(35,1), font = ("italic",18))],
            [sg.Text(pad=(0,3))],
            [sg.Text('Account Name:', font = ("italic",18))], 
            [sg.InputText(key='-Account-', size=(35,1), font = ("italic",18))],
            [sg.Text(pad=(0,3))],
            [sg.Text('Key File:', font = ("italic",18))], 
            [sg.In(key='-Account-', size=(35,1), font = ("italic",18))], 
            [sg.FileBrowse(font = ("italic",18), target=(-1,0))],
           ]

right_col = [[sg.Text('Generate one time password', font = ("italic",25), text_color = "white")],
            [sg.Text(pad=(0,5))],
            [sg.Text('Issuer Name:', font = ("italic",18))], 
            [sg.InputText(key='-Issuer-', size=(35,1), font = ("italic",18))],
            [sg.Text(pad=(0,3))],
            [sg.Text('Account Name:', font = ("italic",18))], 
            [sg.InputText(key='-Account-', size=(35,1), font = ("italic",18))],
            [sg.Text(pad=(0,3))],
            [sg.Text('Key File:', font = ("italic",18))], 
            [sg.In(key='-Account-', size=(35,1), font = ("italic",18))], 
            [sg.FileBrowse(font = ("italic",18), target=(-1,0))],
            [sg.Text(pad=(0,3))],
            [sg.Text('QR Code:', font = ("italic",18))],
            [sg.Image(size=(300,300), filename='MyQRCode.png', key='-IMAGE-')],
            [sg.Text('Complete key here', font = ("italic",18), text_color="white")],
            [sg.Text(pad=(0,3))],
            [sg.Text('Otp Token:', font = ("italic",18))],
            [sg.Text(text=pepe, font = ("italic",45), relief='solid')]
            ]

layout = [  [sg.Text('Time-based One-time Password generator', font = ("italic",50), justification="center", text_color = "yellow")],
            [sg.Text(pad=(0,5))],
            [sg.Column(left_col, element_justification='c'),
             sg.VerticalSeparator(pad=10), 
             sg.Column(right_col, element_justification='c')],
             [sg.VPush()],
            [sg.Button('Ok',font = ("italic",20), size=10), sg.Button('Cancel', font = ("italic",20), size=10)] 
            ]

# Create the Window
window = sg.Window('ft_otp', layout, size=(1100,1100), margins = (20, 20), element_justification='c')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
