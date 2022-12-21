<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="manageChart2" :style="{width:'1500px' , height: '600px'}"></div>
    </div>
  </template>
   
<script setup>
import {watch} from "vue";
const props = defineProps({
  unum: Number,
  snum: Number
})
watch(
//监听props里面的某个对象users，这里是 () =>{return props.users}的简写，
    () => props.snum,
    (newValue, oldValue) => {
      if (newValue > 0) {
        // eslint-disable-next-line @typescript-eslint/no-var-requires
        let echarts = require("echarts");
        let myChart = echarts.init(document.getElementById("manageChart2"));
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
            data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name: '新用户数量',
              type: 'line',
              stack: 'Total',
              data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, props.unum]
            },
            {
              name: '入驻店铺数量',
              type: 'line',
              stack: 'Total',
              data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, props.snum]
            },
          ]
        })
      }
    }
)
  </script>