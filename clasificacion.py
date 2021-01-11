ruta="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\\data limpiada\\CLEAN"
lista_archivos=['1247776452097309.txt','2359787117607181.txt','2338233763157683.txt',
                '2287979277998232.txt','2129766937328183.txt','2111187462511299.txt',
                '1458939510911376.txt','1368421709973017.txt','434584940509838.txt',
                '419397588682810.txt','400986694185111.txt','397393044507256.txt',
                '923913571312203.txt','916830508688464.txt','723574001389336.txt',
                '527422304726461.txt','511908212961170.txt','494724017797129.txt',
                '476340549762452.txt','470984136825431.txt','449254902234199.txt',
                '440949333193574.txt','439692923349814.txt','435667513820648.txt']



for f in lista_archivos:
    total=i = 0
    h1 = h2 = h3 = h4 = h5 = h6 = h7 = h8 = h9 = h10 = h11 =h12=h13=h14=h15=h16=h17=h18=h19=h20=h21=h22=h23=h24=h25=h26=h27=h28=h29=h30=h31=h32=h33=h34=0
    archivo = open(ruta + f, "r", encoding="utf8")
    narchivo = open(ruta+"_" + f, "w", encoding="utf8")
    for linea in archivo.readlines():
        cadena=linea.split("|")
        if(cadena[2].upper().find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA")!=-1):
            h1=h1+1

        elif(cadena[2].upper().find("#PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA")!=-1):
            h2 = h2 + 1
        elif (cadena[2].upper().find("PRENSAVENDIDAPRENSAVENDIDAPRENSAVENDIDA")!=-1):
             h3=h3+1

        elif(cadena[2].upper().find("#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!")!=-1):
            h4 = h4 + 1

        elif (cadena[2].upper().find("ESTÁN INVOLUCRADOS LAS FARC, LATIN KINGS, CUMBIA KINGS, DON GATO Y SU PANDILLA") != -1):
            h5 = h5 + 1

        elif (cadena[2].upper().find("#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA")!=-1):
            h6 = h6 + 1

        elif(cadena[2].upper().find("#PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA ")!=-1):
            h7=h7+1

        elif(cadena[2].upper().find("HTTP")!=-1):
            h8=h8+1

        elif(cadena[2].upper().find("#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA ")!=-1):
            h9=h9+1

        elif(cadena[2].find("#PRENSAVENDIDA# PRENSAVENDIDA#PRENSAVENDIDA")!=-1):
            h10=h10+1

        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA ")!=-1):
            h11=h11+1

        elif(cadena[2].find(" MIS APRECIADOS MEDIOS DE COMUNICACIÓN ")!=-1):
            h12=h12+1

        elif(cadena[2].find(" MI APRECIADO PRESIDENTE ")!=-1):
            h13=h13+1

        elif(cadena[2].find("#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA")!=-1):
            h14=h14+1

        elif(cadena[2].find("#PRENSAVENDIDA#PRENSAVENDIDA#PRENSAVENDIDA")!=-1):
            h15=h15+1

        elif(cadena[2].find("#PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA")!=-1 or cadena[2].find("#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA")!=-1 ):
            h16=h16+1

        elif(cadena[2].find("# PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA")!=-1):
            h17=h17+1

        elif(cadena[2].find("#PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA ")!=-1):
            h18=h18+1

        elif(cadena[2].find("#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA")!=-1):
            h19=h19+1

        elif(cadena[2].find("#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE")!=-1):
            h20=h20+1

        elif(cadena[2].find("#PRENSAHPTA  #PRENSAHPTA  #PRENSAHPTA  #PRENSAHPTA #PRENSAHPTA  ")!=-1):
            h21=h21+1

        elif (cadena[2].find("#LENINTUNOERESMIPRESIDENTE #LENINTUNOERESMIPRESIDENTE#LENINTUNOERESMIPRESIDENTE#LENINTUNOERESMIPRESIDENTE") != -1):
            h22 = h22 + 1
         #   print
        elif(cadena[2].find("#PRENSAVENDIDA #PRENSACORRUPTA #APODÉRATEEC #ÚLTIMAHORA #URGENTE #PAROECUADOREL ODIO HACIA LOS MEDIOS DE COMUNICACIÓN TRADICIONALES EN EL #ECUADOR🇪🇨 VA EN AUMENTO, HACE MINUTOS SE ATACÓ LAS INSTALACIONES DE #TELEAMAZONAS EN EL NORTE DE #QUITO, Y HACE UN MOMENTO DIARIO #ELCOMERCIO DENUNCIÓ QUE GRUPOS DESCONOCIDOS SE ENCUENTRAN ATACANDO SUS INSTALACIONES EN EL SUR SE LE ADVIRTIÓ A LOS MEDIOS PRIVADOS QUE ESTO PODRÍA SUCEDER SI ES QUE NO DECÍAN LA VERDAD AL PAÍS. RECHAZAMOS LOS ACTOS DE VIOLENCIA, PERO DESINFORMARON AL PUEBLO, SE PUSIERON DEL LADO DEL GOBIERNO Y ESTAS SON LAS CONSECUENCIAS.")!=-1):
            h23=h23+1

        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPT #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  ")!=-1):
            h24=h24+1
        elif (cadena[2]==("#PRENSAVENDIDA\n") or cadena[2]==("PRENSAVENDIDA\n") or cadena[2]==("PRENSA VENDIDA\n")):
            h25 = h25 + 1

        elif(cadena[2]==("#PRENSACORRUPTA\n")):
            h26=h26+1

        elif(cadena[2].find("#LENINEBOTLAMISMACOSASON #LENINEBOTLAMISMACOSASON #LENINEBOTLAMISMACOSASON")!=-1):
            h27=h27+1

        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA#PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA#PRENSAVENDIDA#PRENSACORRUPTA")!=-1):
            h28=h28+1

        elif (cadena[2].find("#RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO") != -1):
            h29 = h29 + 1

        elif(cadena[2].find("#FUERALENIN #FUERALENIN #FUERALENIN #FUERALENIN #FUERALENIN")!=-1):
            h30=h30+1

        elif (cadena[2].find("#PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA") != -1):
            h31 = h31 + 1

        elif (cadena[2].find("MI APRECIADA INSIGNIA") != -1):
            h32 = h32 + 1


        elif(cadena[2].find("MI APRECIADA PRENSA") != -1):
            h33 = h33 + 1

        elif(cadena[2].find("😡😡😡😡😡😡\n")!=-1 or cadena[2].find("😡😡😡😡\n")!=-1 or
             cadena[2].find("👎👎👎👎👎👎👎👎👎👎\n")!=-1 or cadena[2].find("🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬\n")!=-1 or
            cadena[2].find("🤮🤮🤮🤮\n")!=-1 or cadena[2].find("🤬🤬🤬🤬🤬\n")!=-1  or cadena[2].find("😠😠😠😠😠\n")!=-1  or
            cadena[2].find("👏👏👏👏👏\n")!=-1 or cadena[2].find("😤😤😤😤😤😤😤😤\n")!=-1 ):
            h34=h34+1
           # print(cadena[2])
        else:
            i = i + 1
          #  print(cadena)
            narchivo.write(str(linea))
           # print(str(i)+"trama"+str(linea))

    total=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20+h21+h22+h23+h24+h25+h26+h27+h28+h29+h30+h31+h32+h33+h34
    print("Nombre de archivo: ",f,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,h31,h32,h33,h34,"total de comentarios borrados: ",total,"n° comentarios limpiados: ",i)