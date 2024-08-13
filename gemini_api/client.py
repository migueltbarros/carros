import google.generativeai as genai


genai.configure(api_key='AIzaSyD__yvW-aivh5H_azG9SovpgxzWnSyiIsU')


def get_car_ai_bio(brand, model, year):
    message = f''' 
    Me mostre uma descrição de venda para o carro {brand} {model} {year}, que apresente o carro de maneira objetiva, mas em apenas 200 caracteres. Fale coisas específicas desse modelo. Descreva especificações técnicas desse modelo de carro. Mesmo com as especificações técnicas, gostaria de um texto limpo e de fácil compreendimento para o possível comprador.
    '''
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message)
    return response.text