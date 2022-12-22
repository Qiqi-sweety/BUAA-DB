<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="storeChart2" :style="{ width: '1500px', height: '600px'}"></div>
    </div>
  </template>

<script setup>
import {reactive, watch} from "vue";
const props = defineProps({
  month_info: Object
})
const data = reactive({
  money: [],
  sales: [],
})
const echarts = require("echarts");

watch(
//监听props里面的某个对象users，这里是 () =>{return props.users}的简写，
    () => props.month_info,
    (newValue, oldValue) => {
      if (newValue.money.length > 0) {
        newValue.money.forEach(item => {
          data.money.push(item)
        })
        newValue.sales.forEach(item => {
          data.sales.push(item)
        })
        let myChart = echarts.init(document.getElementById("storeChart2"));
        // 绘制图表
        myChart.setOption({
          // title: {
          //     text: '订单数量和支出按月统计图'
          // },
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sept','Oct','Nov','Dec']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name: '订单数量',
              type: 'line',
              stack: 'Total',
              data: data.sales
            },
            {
              name: '收入',
              type: 'line',
              stack: 'Total',
              data: data.money
            },
          ]
        })
      }
    }
)

const export_pic = () => {
  let myChart = echarts.init(document.getElementById("storeChart2"));
  const picInfo = myChart.getDataURL({
    type: 'png',
    pixelRatio: 1,
    backgroundColor: '#ffffff',
    // 忽略组件的列表，例如要忽略 toolbox 就是 ['toolbox']
    // excludeComponents: 'toolbox'
  });
  const elink = document.createElement('a');
  elink.download = '图表';
  elink.style.display = 'none';
  elink.href = picInfo;
  document.body.appendChild(elink);
  elink.click();
  URL.revokeObjectURL(elink.href); // 释放URL 对象
  document.body.removeChild(elink)
}

</script>