<template>
  <div class="login-page">
    <a-form
        :model="formState"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 16 }"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
        class="login-form"
    >
      <a-form-item
          label="Username"
          name="username"
          :rules="[{ required: true, message: 'Please input your username!' }]"
      >
        <a-input v-model:value="formState.username"/>
      </a-form-item>

      <a-form-item
          label="Password"
          name="password"
          :rules="[{ required: true, message: 'Please input your password!' }]"
      >
        <a-input-password v-model:value="formState.password"/>
      </a-form-item>

      <a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
        <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
        <a-button type="primary" html-type="submit">Submit</a-button>
      </a-form-item>
    </a-form>


  </div>

</template>
<script setup>
import {reactive, ref} from 'vue';

import http from "../http/index.js";

import {Modal} from 'ant-design-vue'
import setting from "../setting.js";
import router from "../router/index.js";

const formState = reactive({
  username: '',
  password: '',
  remember: false,
});


const onFinish = values => {
  console.log('Success:', values);
  http.post(setting.host + "/users/login", {
    username: values.username,
    password: values.password,

  }).then(response => {
        console.log(response)
        Modal.success({
          title: "系统提示",
          content: "登陆成功"
        })


        localStorage.removeItem("token")
        sessionStorage.removeItem("token")
        if (values.remember) {
          console.log("remember")
          localStorage.setItem("token", response.data.access);
          localStorage.setItem("username", values.username);
        } else {
                    console.log("dontremember")
          sessionStorage.setItem("token", response.data.access);
        }
        router.push('/uric/ShowCenter')
      }
  ).catch(error => {
    Modal.error({
      title: "系统提示",
      content: "用户名密码错误"
    })
  })


};
const onFinishFailed = errorInfo => {
  console.log('Failed:', errorInfo);
};


</script>


<style scoped>
.login-page {
  height: 100vh;
  display: flex;


  align-items: center;
  justify-content: center
}

.login-form {
  width: 300px;

}
</style>