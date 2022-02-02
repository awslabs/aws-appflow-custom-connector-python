echo -e "\033[33m*********** Warning: Please make sure you give correct region, loggroup and Suffix ***********\033[0m"
echo -n "Provide Region:"
read -r
region=$REPLY
echo -n "Provide Loggroup (Should be in the format of /aws/lambda/custom-connector-logging-Aaw0rrvylsya):"
read -r
loggroup=$REPLY
echo -n "Provide name for log file that will be generated:"
read -r
filePath=$REPLY
echo -n "Provide start time (in epoc seconds) for log query:"
read -r
startTime=$REPLY
echo -n "Provide End Time (in epoc seconds) for log query:"
read -r
endTime=$REPLY
read -r -p "Provide Query String:"
query=$REPLY
echo -n "Provide Bucket for log file:"
read -r
bucket=$REPLY
echo -n "Provide number of seconds until the pre-signed URL expires."
read -r
expiryInSeconds=$REPLY
echo -n "Cloudwatch query takes time to execute. The time depends on the interval for which logs are being fetched."
echo -n "Provide wait time (seconds) before query finished."
sleepTime=$REPLY
echo -n "Are above details correct, Please select y/n:"
read -r
if [[ "$REPLY" = "n" ]]; then 
	echo -e "User chose to end the script.Exiting...."
	exit 1
fi
if [[ "$REPLY" != "y" ]]; then
        echo -e "Please type either 'y' on 'n'.Exiting...."
        exit 1
fi
query_response=$(aws logs start-query \
 --region $region \
 --log-group-name $loggroup \
 --start-time $startTime \
 --end-time $endTime \
 --query-string "$query")
query_id=$(echo $query_response | jq -r '.queryId')

echo -e "\033[33m*********** Sleeping for someitme to make sure the query is in complete state ***********\033[0m"
sleep $sleepTime

aws logs get-query-results --query-id $query_id  --region $region > /home/$USER/$filePath

aws s3 cp $filePath s3://$bucket
aws s3 presign s3://$bucket/$filePath --expires-in $expiryInSeconds
