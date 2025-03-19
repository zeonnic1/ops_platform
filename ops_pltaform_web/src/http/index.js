import axios  from "axios";
import setting   from "../setting.js";
const  http =axios.create({
    baseURL:setting.host,
    withCredentials:false
})

//请求拦截器
http.interceptors.request.use((config)=>{
    console.log("http请求之前");
    return config;
    } ,error => {
    console.log("http请求错误")
    return Promise.reject(error)
    }
);

//响应拦截器
http.interceptors.response.use((config)=>{
    console.log("服务器响应之后,返回结果给客户端第一时间 执行then之前");
    return config;
    } ,error => {
    console.log("http响应错误")
    return Promise.reject(error)
    }
);

export  default  http;