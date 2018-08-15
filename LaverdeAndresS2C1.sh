wget https://raw.githubusercontent.com/daniel-lozano/CLASES_PYTHON/master/CLASE1/METODOS/notas.txt

##Punto 1
awk '{if($3>4.0 && $3<5.0)print;}' notas.txt | wc -l > RES1.txt
awk '{if($3>4.0 && $3<5.0 && $6>15.0)print;}' notas.txt | wc -l > RES1.txt

##Punto 2
grep -w "0" notas.txt
awk '{if($7<6.0)print $1, $2;}' notas.txt

##Punto 3
awk '{if($7>8.0)print $1, $7;}' notas.txt > RES2.txt #Imprime apellidos
awk '{if($7>8.0)print;}' notas.txt |wc -l #imprime cantidad
