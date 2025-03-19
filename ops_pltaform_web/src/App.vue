<template>
  <div>
    <a-config-provider :locale="zhCN">
      <router-view/>
    </a-config-provider>
  </div>

</template>

<script setup lang="js">


import zhCN from "ant-design-vue/es/locale/zh_CN";
</script>




