<template>

  <div>
    <a-space wrap>
      <a-button type="primary" @click="get_data">Primary Button</a-button>

    </a-space>
    <a-space direction="vertical" :size="12">
      <a-date-picker v-model:value="value1"/>

    </a-space>
  </div>

  <div class="chart" ref="chart"></div>
</template>


<script setup lang="js">

import {ref} from 'vue';
import http from "../http/index.js";
import zhCN from 'ant-design-vue/es/locale/zh_CN';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import * as echarts from 'echarts';
import {onMounted} from "vue";


const value1 = ref();
const get_data = () => {
  http.get("http://httpbin.org/get").then(
      response => {
        console.log(response.data)
      }
  )
}

var chart = ref()
// 指定图表的配置项和数据
var option = {
  title: {
    text: 'ECharts 入门示例'
  },
  tooltip: {},
  legend: {
    data: ['销量']
  },
  xAxis: {
    data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
};

onMounted(() => {
  let myChart = echarts.init(chart.value)
  myChart.setOption(option)

})
dayjs.locale('zh-cn');
</script>

<style scoped>
.chart {
  width: 500px;
  height: 500px;
  float: left;
  margin: 0 auto 0 100px;
}

</style>