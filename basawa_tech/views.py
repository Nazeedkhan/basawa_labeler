import os
import tempfile
import qrcode
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
import barcode
from barcode.writer import ImageWriter
from .models import First_qr_code_table, Second_qr_code_table, First_bar_code_table, Second_bar_code_table, First_no_code_table, Second_no_code_table

def home_page(request):
    return render(request, "template.html", {})

def form_page1(request):
    return render(request, "showforms/form1.html",{})
def form_page2(request):
    return render(request, "showforms/form2.html",{})
def form_page3(request):
    return render(request, "showforms/form3.html",{})
def form_page4(request):
    return render(request, "showforms/form4.html",{})
def form_page5(request):
    return render(request, "showforms/form5.html",{})
def form_page6(request):
    return render(request, "showforms/form6.html",{})


def show_pdf1(request):
    template = get_template('pdfforms/pdf_form1.html')
    qrcode_value = request.POST['qrcode1']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']

    db = First_qr_code_table(qrcode=qrcode_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value)
    db.save()
    # Create a temporary directory for storing files
    temp_dir = tempfile.mkdtemp()
    try:
        # Generate QR code on the server side
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qrcode_value)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        # Create a temporary file path within the temporary directory
        qr_img_path = os.path.join(temp_dir, 'qr_code.png')
        # Save QR code image to the temporary file path
        qr_img.save(qr_img_path)
        context = {
            'qrcode_value': qrcode_value,
            'field1_value': field1_value,
            'value1_value': value1_value,
            'field2_value': field2_value,
            'value2_value': value2_value,
            'field3_value': field3_value,
            'value3_value': value3_value,
            'qr_code_path': qr_img_path,
        }
        html_content = template.render(context)
        pdf_response = HttpResponse(content_type='application/pdf')
        pisa.CreatePDF(html_content, dest=pdf_response)
        return pdf_response
    finally:
        # Clean up: Remove the temporary directory and its contents
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            os.remove(file_path)
        os.rmdir(temp_dir)

def show_pdf2(request):
    template = get_template('pdfforms/pdf_form2.html')
    qrcode_value = request.POST['qrcode1']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']

    db = Second_qr_code_table(qrcode=qrcode_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value)
    db.save()

    # Create a temporary directory for storing files
    temp_dir = tempfile.mkdtemp()
    try:
        # Generate QR code on the server side
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qrcode_value)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        # Create a temporary file path within the temporary directory
        qr_img_path = os.path.join(temp_dir, 'qr_code.png')
        # Save QR code image to the temporary file path
        qr_img.save(qr_img_path)
        context = {
            'qrcode_value': qrcode_value,
            'field1_value': field1_value,
            'value1_value': value1_value,
            'field2_value': field2_value,
            'value2_value': value2_value,
            'field3_value': field3_value,
            'value3_value': value3_value,
            'qr_code_path': qr_img_path,
        }
        html_content = template.render(context)
        pdf_response = HttpResponse(content_type='application/pdf')
        pisa.CreatePDF(html_content, dest=pdf_response)
        return pdf_response
    finally:
        # Clean up: Remove the temporary directory and its contents
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            os.remove(file_path)
        os.rmdir(temp_dir)

        
        
        









def show_pdf3(request):
    template = get_template('pdfforms/pdf_form3.html')
    code_value = request.POST['barcode1']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']

    db = First_bar_code_table(qrcode=code_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value)
    db.save()

    # Create a temporary directory for storing files
    temp_dir = tempfile.mkdtemp()
    try:
        # Generate barcode on the server side
        ean = barcode.get_barcode_class('code128')  # You can choose a different barcode format
        ean_instance = ean(code_value, writer=ImageWriter())
        barcode_img_path = os.path.join(temp_dir, 'barcode.png')
        ean_instance.save(barcode_img_path)

        context = {
            'code_value': code_value,
            'field1_value': field1_value,
            'value1_value': value1_value,
            'field2_value': field2_value,
            'value2_value': value2_value,
            'field3_value': field3_value,
            'value3_value': value3_value,
            'barcode_path': barcode_img_path,
        }

        # Render the template with the context
        html_content = template.render(context)

        # Create a response object with PDF mime type
        pdf_response = HttpResponse(content_type='application/pdf')

        # Use pisa to generate PDF from HTML content
        pisa.CreatePDF(html_content, dest=pdf_response)

        return pdf_response
    finally:
        # Clean up: Remove the temporary directory and its contents
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            os.remove(file_path)
        os.rmdir(temp_dir)



def show_pdf4(request):
    template = get_template('pdfforms/pdf_form4.html')
    code_value = request.POST['barcode2']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']

    db = Second_bar_code_table(qrcode=code_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value)
    db.save()

    temp_dir = tempfile.mkdtemp()
    try:
        ean = barcode.get_barcode_class('code128') 
        ean_instance = ean(code_value, writer=ImageWriter())
        barcode_img_path = os.path.join(temp_dir, 'barcode.png')
        ean_instance.save(barcode_img_path)

        context = {
            'code_value': code_value,
            'field1_value': field1_value,
            'value1_value': value1_value,
            'field2_value': field2_value,
            'value2_value': value2_value,
            'field3_value': field3_value,
            'value3_value': value3_value,
            'barcode_path': barcode_img_path,
        }

        # Render the template with the context
        html_content = template.render(context)

        # Create a response object with PDF mime type
        pdf_response = HttpResponse(content_type='application/pdf')

        # Use pisa to generate PDF from HTML content
        pisa.CreatePDF(html_content, dest=pdf_response)

        return pdf_response
    finally:
        # Clean up: Remove the temporary directory and its contents
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            os.remove(file_path)
        os.rmdir(temp_dir)


def show_pdf5(request):
    template = get_template('pdfforms/pdf_form5.html')
    code_value = request.POST['qrcode1']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']
    field4_value = request.POST['field4']
    value4_value = request.POST['value4']

    db = First_no_code_table(qrcode=code_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value, field4=field4_value , value4=value4_value)
    db.save()

    context = {
        'code_value': code_value,
        'field1_value': field1_value,
        'value1_value': value1_value,
        'field2_value': field2_value,
        'value2_value': value2_value,
        'field3_value': field3_value,
        'value3_value': value3_value,
        'field4_value': field4_value,
        'value4_value': value4_value,
    }
    html_content = template.render(context)
    pdf_response = HttpResponse(content_type='application/pdf')
    pisa.CreatePDF(html_content, dest=pdf_response)

    return pdf_response


def show_pdf6(request):
    template = get_template('pdfforms/pdf_form6.html')
    code_value = request.POST['qrcode1']
    field1_value = request.POST['field1']
    value1_value = request.POST['value1']
    field2_value = request.POST['field2']
    value2_value = request.POST['value2']
    field3_value = request.POST['field3']
    value3_value = request.POST['value3']

    db = Second_no_code_table(qrcode=code_value, field1=field1_value, value1=value1_value, field2=field2_value, value2=value2_value, field3=field3_value, value3=value3_value)
    db.save()

    context = {
        'code_value': code_value,
        'field1_value': field1_value,
        'value1_value': value1_value,
        'field2_value': field2_value,
        'value2_value': value2_value,
        'field3_value': field3_value,
        'value3_value': value3_value,
    }
    
    html_content = template.render(context)
    pdf_response = HttpResponse(content_type='application/pdf')
    pisa.CreatePDF(html_content, dest=pdf_response)

    return pdf_response3