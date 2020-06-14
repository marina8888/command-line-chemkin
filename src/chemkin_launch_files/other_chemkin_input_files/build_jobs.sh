

for filename in ./input_files/*.inp; do
    cp ./peach.sh "./job_files/$(basename "$filename" .inp).sh"
    echo "CKReactorBurnerStabilizedStagnationFlame < "$filename" > "./solutions/$(basename "$filename" .inp).out"" >> "./job_files/$(basename "$filename" .inp).sh"
done
