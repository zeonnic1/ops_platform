<template>
    <a-form>
      <a-row :span="6">
        <div class="add_host" style="margin:15px;">
          <a-button @click="handleAdd" type="primary">
            <PlusOutlined/>
            新建
          </a-button>
        </div>
        <div class="add_hosts" style="margin:15px;">
          <a-button @click="handleImport" type="primary">
            <CloudUploadOutlined/>
            批量导入
          </a-button>
        </div>
      </a-row>
    </a-form>

  <a-table :columns="columns" :dataSource="host_list.data" row-key="id">
    <template v-slot:bodyCell="{column, record}">
      <template v-if="column.dataIndex === 'action'">
        <a-popconfirm title="sure to delete？" @confirm="deleteHost(record)">
          <a style="color: black">Delete</a>
        </a-popconfirm>
      </template>
    </template>
  </a-table>

    <a-modal v-model:open="hostsVisble" title="新建主机信息" @ok="handle_hosts">
      <a-form :label-col="{ span: 6 }"
              :wrapper-col="{ span: 18 }"
              :ok-button-props="{ disabled: true }"
              :cancel-button-props="{ disabled: true }"
              class="add_host"
      >
        <a-form-item label="主机类别">

          <a-select v-model="category"
                    placeholder="请输入主机类别"
                    ref="select"
                    show-search
                    :options="items.map(item => ({ value: item }))"
          >
            <template #dropdownRender="{ menuNode: menu }">
              <!--            <v-nodes :vnodes="menu"/>-->
              <a-divider style="margin: 4px 0"/>
              <a-space style="padding: 4px 8px">
                <a-input ref="inputRef" v-model:value="name" placeholder="Please enter item"/>
                <a-button type="text" @click="addItem">
                  <template #icon>
                    <plus-outlined/>
                  </template>
                  Add item
                </a-button>
              </a-space>
            </template>
          </a-select>

        </a-form-item>
        <a-form-item label="ip地址">
          <a-input v-model="ipAddress" placeholder="请输入ip">
          </a-input>
        </a-form-item>
        <a-form-item label="端口">
          <a-input v-model="port" placeholder="请输入port">
          </a-input>
        </a-form-item>

        <a-form-item label="备注">
          <a-input v-model="remark" style="height: 100px">
          </a-input>
        </a-form-item>

      </a-form>
    </a-modal>
</template>


<script setup>
import {PlusOutlined, CloudUploadOutlined} from "@ant-design/icons-vue"
import {reactive, ref, toRefs, defineComponent, onMounted, nextTick} from "vue";
import http from "../http/index.js";
import setting from "../setting.js";

// const VNodes = defineComponent({
//   props: {
//     vnodes: {
//       type: Object,
//       required: true,
//     },
//   },
//   render() {
//     return this.vnodes;
//   },
// });

const columns = [
  {
    title: 'ip_addr',
    dataIndex: 'ip_addr',
  },
  {
    title: 'port',
    dataIndex: 'port',
  },
  {
    title: 'category',
    dataIndex: 'category',
  },
  {
    title: 'username',
    dataIndex: 'username',
  },
  {
    title: 'action',
    dataIndex: 'action',
  }
];
var host_list = reactive({data: []})

let index = 0;
const items = ref(['数据库服务器', '前端服务器', '缓存服务器']);
const category = ref();
const inputRef = ref();
const name = ref();
const addItem = e => {
  e.preventDefault();
  console.log('addItem');
  items.push(name.value || `New item ${(index += 1)}`);
  name.value = '';
  setTimeout(() => {
    inputRef.value?.focus();
  }, 0);
};


const handle_hosts = e => {
  console.log(e.value);
  hostsVisble.value = false;

};

const get_data_list = () => {
  nextTick(() => {
    let token = localStorage.getItem("token") || sessionStorage.getItem("token")
    http.get(setting.host + "/hosts", {
      headers: {
        Authorization: "Bearer" + token
      }
    }).then(response => {
      host_list.data = response.results
    })
  })

}


const hostsVisble = ref(false)

const handleAdd = () => {
  hostsVisble.value = true
}
const resetForm = () => {

}
const deleteHost = (record) => {
  console.log(record)
  http.delete(`${setting.host}/hosts/${record.id}`).then(() => {
    resetForm()

  })
}
const handleImport = () => {

}

onMounted(() => {
  get_data_list()
})
</script>

<style scoped>
.add_host {
  width: 300px;
  margin: 20px auto;

}

</style>