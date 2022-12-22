<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="storeChart1" :style="{ width: '1500px', height: '500px'}"></div>
    </div>
</template>
   
<script setup>
import {reactive, watch} from "vue";
const props = defineProps({
  item_sales: Object
})
const data = reactive({
  name: [],
  sales: [],
})

watch(
    () => props.item_sales,
    (newValue, oldValue) => {
      if (newValue.item_name.length > 0) {
        newValue.item_name.forEach(item => {
          data.name.push(item)
        })
        newValue.sales.forEach(item => {
          data.sales.push(item)
        })
        // eslint-disable-next-line @typescript-eslint/no-var-requires
        let echarts = require("echarts");
        let myChart = echarts.init(document.getElementById("storeChart1"));
        // 绘制图表
        myChart.setOption({
          title: {
            text: '商品销量图'
          },
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          xAxis: {
            data: data.name
          },
          yAxis: {},
          series: [
            {
              type: 'bar',
              data: data.sales
            }
          ]
        })
      }
    }
)
</script>