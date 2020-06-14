
for filename in ./job_files/*.sh; do
    qsub "$filename"
done
