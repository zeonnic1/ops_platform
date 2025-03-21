<template>
  <a-layout>
    <a-layout-sider class="siderStyle">
      <div class="logo">
        <a-button @click="toggleCollapsed">
          <MenuUnfoldOutlined v-if="state.collapsed"/>
          <MenuFoldOutlined v-else/>
        </a-button>
        运维平台
      </div>
      <a-menu
          v-model:selectedKeys="state.selectedKeys" theme="dark"
          mode="inline"
          :open-keys="state.openKeys"
          :items="items"
          @click="handleClick"
      ></a-menu>
    </a-layout-sider>

    <a-layout class="layoutStyle">
      <a-layout-header class="headerStyle">
        <a-breadcrumb>
          <a-breadcrumb-item>{{ Title }}</a-breadcrumb-item>
        </a-breadcrumb>
        <div>
          <a-avatar>{{ get_username() }}</a-avatar>
          <a-button type="primary" @click="logout" class="logout">注销</a-button>
        </div>
      </a-layout-header>

      <a-layout-content class="contentStyle">
        <router-view></router-view>
      </a-layout-content>

      <a-layout-footer class="footerStyle">Ant Design ©2018 Created by Ant UED</a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup name="Layout">
import {ref, reactive, h, watch, createVNode, onMounted,} from 'vue';
import {
  MenuUnfoldOutlined, MenuFoldOutlined, PieChartOutlined, DesktopOutlined, InboxOutlined,
  MailOutlined,
  AppstoreOutlined, ExclamationCircleOutlined,
} from '@ant-design/icons-vue';
// import router from "../router/index.js";
import {Modal} from "ant-design-vue";
import {useRoute} from "vue-router";
import router from "../router/index.js";

const route = useRoute()

const collapsed = ref(false);
const Title = route.meta.title
const get_username = () => {

  return localStorage.getItem("username")

}

function logout() {
  console.log('click logout',);
  Modal.confirm({
    title: 'Confirm',
    icon: createVNode(ExclamationCircleOutlined),
    content: '确认注销?',
    okText: '确认',
    cancelText: '取消',
    onOk() {
      localStorage.removeItem("token")
      sessionStorage.removeItem("token")
      router.push("/login")
    }
  })

}

const state = reactive({
  collapsed: false,
  selectedKeys: ['1'],
  openKeys: ['sub1'],
  preOpenKeys: ['sub1'],
});

function handleClick(info) {
  console.log('click', info.item.menu_url);
  router.push({path: info.item.menu_url})
  // router.getRoutes(info.item.menu_url)
}


const items = reactive([
  {
    key: '1',
    icon: () => h(PieChartOutlined),
    label: '展示中心',
    title: 'ShowCenter',
    menu_url: '/uric/show_center'
  },
  {
    key: '2',
    icon: () => h(DesktopOutlined),
    label: '资产管理',
    title: 'hosts',
    menu_url: '/uric/hosts'
  },
  {
    key: '3',
    icon: () => h(InboxOutlined),
    label: '数量任务',
    title: 'Option 3',
  },
  {
    key: 'sub1',
    icon: () => h(MailOutlined),
    label: '代码发布',
    title: 'coding',
    children: [
      {
        key: '5',
        label: '拉分支',
        title: 'Option 5',
      },
      {
        key: '6',
        label: '推送',
        title: 'Option 6',
      },
      {
        key: '7',
        label: '克隆',
        title: 'Option 7',
      },
      {
        key: '8',
        label: 'jenkins',
        title: 'Option 8',
      },
    ],
  },
  {
    key: 'sub2',
    icon: () => h(AppstoreOutlined),
    label: '定时任务',
    title: 'crontab',

  },
  {
    key: 'sub3',
    label: '用户管理',
    title: 'Submenu',
    children: [
      {
        key: '11',
        label: '角色管理',
        title: 'Option 11',
      },
      {
        key: '12',
        label: '系统设置',
        title: 'Option 12',
      }
    ],
  },
]);
watch(
    () => state.openKeys,
    (_val, oldVal) => {
      state.preOpenKeys = oldVal;
    },
);
const toggleCollapsed = () => {
  state.collapsed = !state.collapsed;
  state.openKeys = state.collapsed ? [] : state.preOpenKeys;
};

</script>

<style scoped>

.siderStyle {
  .logo {
    height: 52px;
    display: flex;
    align-items: center;
    color: #fff;
  }
}

.headerStyle {
  height: 52px;
  background-color: #fff;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-inline: 21px;

  .logout {
    margin-left: 10px;
  }
}

.layoutStyle {
  background-color: #f8f8f8;

  .contentStyle {
    height: calc(100vh - 120px);
    background-color: #fff;
    margin: 10px;
  }

  .footerStyle {
    height: 18px;
    line-height: 18px;
    font-size: 12px;
  }
}


:deep(.ant-btn-default) {
  background-color: transparent !important;
  border-color: transparent !important;
}

:deep(.ant-btn) {
  color: #fff !important;
}

</style>