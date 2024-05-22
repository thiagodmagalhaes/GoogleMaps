import time
import pandas as pd

from playwright.sync_api import sync_playwright


def buscar_geolocalizacao(nomefantasia, endereco_receita_federal):
    
    with sync_playwright() as p:
        #Criando, abrindo navegandor e acessando a página do google maps
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://www.google.com/maps"

        #Verifica se conseguiu acessar a página(URL) do google maps
        try:
            page.goto(url)
        except:
            print('\n\nERRO: Não foi possível acessar o link: {}\nVerifique sua conexão com a internet!\n\n\n'.format(url))
            return None
        texto = f"{nomefantasia + " " + endereco_receita_federal}"

        try:
            #Insere no campo de pesquisa o Nome e Endereço do estabelecimento e clica para "pesquisar"
            page.fill('//*[@id="searchboxinput"]', texto)
            page.click('//*[@id="searchbox-searchbutton"]')


            # Verifica se o estabelecimento existe por meio da tag HTML: 'rogA2c'
            try:
                page.wait_for_selector('.rogA2c')
            except:
                print('\nLocal não encontrado!!!')
                return None
            
            time.sleep(3)  # Tempo adicional de espera após o HTML estar presente para carregar todos dados

            # AGORA ELE COLETA AS INFORMAÇÕES DE CADA TAG HTML ESPECÍFICA PARA ENDEREÇO, NÚMERO DE TELEFONE
            # COLETA TODAS INFORMAÇÕES DISPONÍVEIS DO ESTABELECIMENTO QUE SE ENCONTRA NO GOOGLE MAPS
            # CADA INFORMAÇÃO É ARMAZENADA EM SUA RESPECTIVA VARIÁVEL
            
            endereco_google = page.inner_text('button[aria-label^="Endereço:"] .Io6YTe')
            data_item_id = page.get_attribute('button[aria-label^="Telefone:"]', 'data-item-id')
            telefone_google = data_item_id.split(':')[-1] 
            nomeFantasia_google = page.inner_text('//h1[@class="DUwDvf lfPIob"]')
            page.click('span[aria-label^="Mostrar horário de funcionamento da semana"]')
            horario_funcionamento = page.inner_text('div[aria-label] .t39EBf.GUrTXd')
            print('\n\nHorario funcionamento: ',horario_funcionamento)


            facebook_element = page.query_selector('a[href*="facebook.com"]')
            whatsapp_element = page.query_selector('a[href*="whatsapp.com"]')
            instagram_element = page.query_selector('a[href*="instagram.com"]')



            #CRIA VARIÁVEIS COM "N/A - NULO" PARA IDENTIFICAR SE O LOCAL POSSUI WHATAPPS OU REDE SOCIAL
            rede_social = 'N/A'
            has_whatsapp = 'N/A'

            #OBTÉM O LINK DO WHATSAPP/REDE SOCIAL CASO TENHA E GRAVA NAS RESPECTIVAS VARIÁVEIS
            if facebook_element:
                rede_social = facebook_element.get_attribute('href')
                print("FACEBOOK: ", rede_social)
            if instagram_element:
                rede_social = instagram_element.get_attribute('href')
                print("INSTAGRAM: ", rede_social)
            if whatsapp_element:
                has_whatsapp = whatsapp_element.get_attribute('href')
                print("WHATAPPS: ", has_whatsapp)



            #CLICA EM "SOBRE" ONDE CONTÉM INFORMAÇÕES SOBRE ACESSIBILIDADE, TIPOS DE CARDÁPIO E ENTRE OUTROS
            page.click('button[aria-label^="Sobre"]')

            #ESPERA PELA CLASSE "SOBRE" PARA EXTRIAR AS INFORMAÇÕES DESEJADAS
            page.wait_for_selector('.ZQ6we')

            # EXTRAI TODAS INFORMAÇÕES PRESENTES EM "SOBRE", CASO TENHA
            # PARA CADA INFORMAÇÃO É ARMAZENADA EM UMA VARIÁVEL
            serves_dine_in_element = page.query_selector('span[aria-label="Serve jantar"]')
            has_takeout_element = page.query_selector('span[aria-label="Comida para viagem"]')
            has_delivery_element = page.query_selector('span[aria-label="Faz entrega"]')
            has_in_store_pickup_element = page.query_selector('span[aria-label="Oferece retirada na porta"]')
            digital_payment_options_element = page.query_selector('span[aria-label="Aceita cartões de crédito"]')
            digital_payment_options_element2 = page.query_selector('span[aria-label="Cartões de crédito"]')
            digital_payment_options_element3 = page.query_selector('span[aria-label="Aceita cartões de débito"]')
            digital_payment_options_element4 = page.query_selector('span[aria-label="Cartões de débito"]')
            has_all_you_can_eat_always_element = page.query_selector('span[aria-label="Tem buffet à vontade"]')
            has_bar_onsite_element = page.query_selector('span[aria-label="Tem bar no local"]')
            has_braille_menu_element = page.query_selector('span[aria-label="Tem menu em braile"]')
            has_childrens_menu_element = page.query_selector('span[aria-label="Tem cardápio infantil"]')
            has_drive_through_element = page.query_selector('span[aria-label="Tem drive-through"]')
            requires_reservation_element = page.query_selector('span[aria-label="Aceita reservas"]')
            serves_alcohol_element = page.query_selector('span[aria-label="Serve bebidas alcoólicas"]')
            serves_cocktails_element = page.query_selector('span[aria-label="Serve coquetéis"]')
            serves_halal_food_element = page.query_selector('span[aria-label="Serve alimentos halal"]')
            serves_happy_hour_drinks_element = page.query_selector('span[aria-label="Serve bebidas para happy hour"]')
            serves_happy_hour_food_element = page.query_selector('span[aria-label="Serve pratos para happy hour"]')
            serves_late_night_food_element = page.query_selector('span[aria-label="Serve comida tarde da noite"]')
            serves_liquor_element = page.query_selector('span[aria-label="Serve licor"]')
            serves_organic_element = page.query_selector('span[aria-label="Serve pratos orgânicos"]')
            serves_vegetarian_element = page.query_selector('span[aria-label="Serve pratos vegetarianos"]')
            serves_wine_element = page.query_selector('span[aria-label="Serve vinho"]')
            welcomes_children_element = page.query_selector('span[aria-label="Bom para ir com crianças"]')
            has_restroom_element = page.query_selector('span[aria-label="Tem banheiro"]')
            has_high_chairs_element = page.query_selector('span[aria-label="Tem cadeirinhas altas"]')
            is_wheelchair_accessible_element = page.query_selector('span[aria-label="Tem entrada com acessibilidade"]')
            

            # GRAVA EM SUAS RESPECTIVAS VARIÁVEIS CADA INFORMAÇÃO OBTIDA NO SITE
            # SE TEM A INFORMAÇÃO GRAVA "Yes" , CASO NÃO TENHA GRAVA "No" EM CADA CAMPO
            if has_delivery_element:
                has_delivery = 'Yes'
            else:
                has_delivery = 'No'
            if serves_dine_in_element:
                serves_dine_in = 'Yes'
            else:
                serves_dine_in = 'No'
            if serves_cocktails_element:
                serves_cocktails = 'Yes'
            else:
                serves_cocktails = 'No'
            if has_takeout_element:
                has_takeout = 'Yes'
            else:
                has_takeout = 'No'
            if has_in_store_pickup_element:
                has_in_store_pickup = 'Yes'
            else:
                has_in_store_pickup = 'No'
            if digital_payment_options_element or digital_payment_options_element2 or digital_payment_options_element3 or digital_payment_options_element4:
                digital_payment_options = 'Yes'
            else:
                digital_payment_options = 'No'
            if has_all_you_can_eat_always_element:
                has_all_you_can_eat_always = 'Yes'
            else:
                has_all_you_can_eat_always = 'No'
            if has_bar_onsite_element:
                has_bar_onsite = 'Yes'
            else:
                has_bar_onsite = 'No'
            if has_braille_menu_element:
                has_braille_menu = 'Yes'
            else:
                has_braille_menu = 'No'
            if has_childrens_menu_element:
                has_childrens_menu = 'Yes'
            else:
                has_childrens_menu = 'No'
            if has_drive_through_element:
                has_drive_through = 'Yes'
            else:
                has_drive_through = 'No'
            if requires_reservation_element:
                requires_reservation = 'Yes'
            else:
                requires_reservation = 'No'
            if serves_alcohol_element:
                serves_alcohol = 'Yes'
            else:
                serves_alcohol = 'No'
            if serves_halal_food_element:
                serves_halal_food = 'Yes'
            else:
                serves_halal_food = 'No'
            if serves_happy_hour_drinks_element:
                serves_happy_hour_drinks = 'Yes'
            else:
                serves_happy_hour_drinks = 'No'
            if serves_happy_hour_food_element:
                serves_happy_hour_food = 'Yes'
            else:
                serves_happy_hour_food = 'No'
            if serves_late_night_food_element:
                serves_late_night_food = 'Yes'
            else:
                serves_late_night_food = 'No'
            if serves_liquor_element:
                serves_liquor = 'Yes'
            else:
                serves_liquor = 'No'
            if serves_organic_element:
                serves_organic = 'Yes'
            else:
                serves_organic = 'No'
            if serves_vegetarian_element:
                serves_vegetarian = 'Yes'
            else:
                serves_vegetarian = 'No'
            if serves_wine_element:
                serves_wine = 'Yes'
            else:
                serves_wine = 'No'
            if welcomes_children_element:
                welcomes_children = 'Yes'
            else:
                welcomes_children = 'No'
            if has_restroom_element:
                has_restroom = 'Yes'
            else:
                has_restroom = 'No'
            if has_high_chairs_element:
                has_high_chairs = 'Yes'
            else:
                has_high_chairs = 'No'
            if is_wheelchair_accessible_element:
                is_wheelchair_accessible = 'Yes'
            else:
                is_wheelchair_accessible = 'No'


            #GRAVA CADA DADO EXTRAIDO DO SITE EM UM CAMPO, DESDE DO NOME, TELEFONE, ENDEREÇO
            #ATÉ COMO ACESSIBILIDADE, TIPO DE CARDÁPIOS, HORÀRIOS DE FUNCIONAMENTO E ENTRE OUTROS
            if any(word in endereco_google for word in texto.split()):
                dados = {
                    'Name': nomeFantasia_google,
                    'Full_Address': endereco_google,
                    'Phone': telefone_google,                    
                    'rede_social': rede_social,
                    'whatapps': has_whatsapp,
                    'opening_hours': horario_funcionamento,
                    'serves_dine_in': serves_dine_in,
                    'has_takeout': has_takeout,
                    'has_delivery': has_delivery,
                    'has_in_store_pickup': has_in_store_pickup,
                    'digital_payment_options': digital_payment_options,
                    'has_all_you_can_eat_always': has_all_you_can_eat_always,
                    'has_bar_onsite': has_bar_onsite,
                    'has_braille_menu': has_braille_menu,
                    'has_childrens_menu': has_childrens_menu,
                    'has_drive_through': has_drive_through,
                    'requires_reservation': requires_reservation,
                    'serves_alcohol': serves_alcohol,
                    'serves_cocktails': serves_cocktails,
                    'serves_halal_food': serves_halal_food,
                    'serves_happy_hour_drinks': serves_happy_hour_drinks,
                    'serves_happy_hour_food': serves_happy_hour_food,
                    'serves_late_night_food': serves_late_night_food,
                    'serves_liquor': serves_liquor,
                    'serves_organic': serves_organic,
                    'serves_vegetarian': serves_vegetarian,
                    'serves_wine': serves_wine,
                    'welcomes_children': welcomes_children,
                    'has_restroom': has_restroom,
                    'has_high_chairs': has_high_chairs,
                    'is_wheelchair_accessible': is_wheelchair_accessible


                }
                return dados

        except Exception as e:
            print(f"Erro: {e}")
        browser.close()#-
