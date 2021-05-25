start=`date +%s`
echo "test"
sleep 5
end=`date +%s`
runtime=$((end-start))
echo "runtime: $runtime seconds"
