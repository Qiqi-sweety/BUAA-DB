<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="manageChart1" :style="{width:'1500px', height: '500px'}"></div>
    </div>
  </template>
   
<script setup>
import {reactive, watch} from "vue";
const props = defineProps({
  store_list: Object
})
const data = reactive({
  store_list: [['store', '总销量', '总收入', '平均评分'], ]
})

watch(
//监听props里面的某个对象users，这里是 () =>{return props.users}的简写，
    () => props.store_list.s,
    (newValue, oldValue) => {
      if (newValue.length > 0) {
        newValue.forEach(item => {
          data.store_list.push(item)
        })
        // eslint-disable-next-line @typescript-eslint/no-var-requires
        let echarts = require("echarts");
        let myChart = echarts.init(document.getElementById("manageChart1"));
        // 绘制图表
        myChart.setOption({
          title: {
              text: '店铺数据统计图'
          },
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          dataset: {
            source: data.store_list
          },
          xAxis: { type: 'category' },
          yAxis: {},
          // Declare several bar series, each will be mapped
          // to a column of dataset.source by default.
          series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }],
        });
    }
})
</script>