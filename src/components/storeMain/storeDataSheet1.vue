<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="8"
        style = "padding-left: 10%;padding-top: 40px ;height: 140px">
          <n-statistic label="历史订单数量">
            {{ info.orders_num }}
          </n-statistic>
        </el-col>
      
        <el-col :span="8" 
        style="padding-left:10%;padding-top: 40px;">
          <n-statistic label="平均评分">
            ⭐{{ info.star }}
          </n-statistic>
        </el-col>
        <el-col :span="8" 
        style="padding-left:10%;padding-top: 40px;">
          <n-statistic label="历史收入">
            ￥{{ info.income }}
          </n-statistic>
        </el-col>


        
    </el-row>
    <el-row>
      <n-button type="warning"
                style="margin-left:90%;margin-top:20px"
                @click="export_pic('1')"
      >导出图表</n-button>
    </el-row>
    <el-row>
      <storeChart1 style="background-color:white;border-radius: 20px;margin-top: 20px;" :item_sales="info.item_sales_list"/>
    </el-row>
    <el-row>
      <n-button type="warning"
                style="margin-left:90%;margin-top:20px"
                @click="export_pic('2')"
      >导出图表</n-button>
    </el-row>
    <el-row>
      <storeChart2 style="background-color:white;border-radius: 20px;margin-top: 20px;" :month_info="info.month_info"/>
    </el-row>
    
    
</template>

<script setup>
import {NStatistic,NButton} from 'naive-ui'
import StoreChart1 from './storeChart1.vue';
import StoreChart2 from './storeChart2.vue';
import {onMounted, reactive} from "vue";
import {show_data} from "@/api/store";
const info = reactive({
  orders_num: 0,
  star: 0.0,
  favorite_item: {},
  item_sales_list: {},
  month_info: {},
  income: 0
})
const echarts = require("echarts");
const export_pic = (id) => {
  let myChart = echarts.init(document.getElementById("storeChart" + id));
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


onMounted(() => {
  show_data().then(res => {
    let content = res.data
    console.log(content)
    if (res) {
      info.orders_num = content.orders_num
      info.star = content.star
      info.favorite_item = content.favorite_item
      info.item_sales_list = content.item_sales_list
      info.month_info = content.month_info
      info.income = content.income
    }
  })
})

</script>