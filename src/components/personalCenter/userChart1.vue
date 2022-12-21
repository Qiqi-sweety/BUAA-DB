<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="userChart1" :style="{ width: '500px', height: '500px'}"></div>
    </div>
  </template>
   
<script>
export default {
  name: "userChart1",
  mounted() {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    let echarts = require("echarts");
    let myChart = echarts.init(document.getElementById("userChart1"));
    // 绘制图表
    myChart.setOption({
      title: {
          text: '订单价格分布图'
      },
      tooltip: {
        trigger: "item",
      },
      legend: {
        top: "5%",
        left: "center",
      },
      series: [
        {
          name: "Access From",
          type: "pie",
          radius: ["40%", "70%"],
          avoidLabelOverlap: false,
          label: {
            show: false,
            position: "center",
          },
          emphasis: {
            label: {
              show: true,
              fontSize: "40",
              fontWeight: "bold",
            },
          },
          labelLine: {
            show: false,
          },
          data: [
            { value: 1048, name: "￥10以下" },
            { value: 735, name: "￥10到￥30" },
            { value: 580, name: "￥30到￥50" },
            { value: 484, name: "￥50到￥100" },
            { value: 300, name: "￥100以上" },
          ],
        },
      ],
    });
  },
};
</script>