for i in 1 2 4 8 
do
 rm -r "stdc_1f${i}t"
 mkdir "stdc_1f${i}t"
 cd "stdc_1f${i}t"
 echo "stdc_1f${i}t"
 python3 ../test_trigP1_v1Dev_build.py 1 ${i}
 cd ..
done

for i in 1 2 4 
do
 rm -r "stdc_2f${i}t"
 mkdir "stdc_2f${i}t"
 cd "stdc_2f${i}t"
 echo "stdc_2f${i}t"
 python3 ../test_trigP1_v1Dev_build.py 2 ${i}
 cd ..
done

for i in 1 2 
do
 rm -r "stdc_4f${i}t"
 mkdir "stdc_4f${i}t"
 cd "stdc_4f${i}t"
 echo "stdc_4f${i}t"
 python3 ../test_trigP1_v1Dev_build.py 4 ${i}
 cd ..
done

rm -r "stdc_8f1t"
mkdir "stdc_8f1t"
cd "stdc_8f1t"
echo "stdc_8f1t"
python3 ../test_trigP1_v1Dev_build.py 8 1
cd .. 

