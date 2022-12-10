<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="storeChart1" :style="{ width: '1500px', height: '500px'}"></div>
    </div>
  </template>
   
  <script>
  export default {
    name: "storeChart1",
    mounted() {
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
            data: ['多肉葡萄', '烤黑糖波波牛乳', '芋泥牛乳茶', '纯牛乳茶', '芝芝多肉青提', '波波咖啡', '椰椰雪糕杯','多肉大橘']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25,100]
    }
  ],
      });
    },
  };
  </script>