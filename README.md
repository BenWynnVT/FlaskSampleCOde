# FlaskSampleCode


## input-methods.py
Here are some cURL commands you can use to query the input methods example.

cURL Example: 
```{bash}
curl --location --request POST http://127.0.0.1:5000/ --header 'Content-Type:image/jpeg' --data-binary "@Downloads/FlaskSampleCode-main/FlaskSampleCode-main/images/image.jpg" --output "Downloads/FlaskSampleCode-main/FlaskSampleCode-main/images/output.jpg"
```

```{bash}
curl --location --request POST http://127.0.0.1:5000/birthday --header "Content-Type:application/json" --data "{\"birthday\":\"1/1/1900\", \"first\":\"Jane\", \"last\":\"Doe\"}"
```
