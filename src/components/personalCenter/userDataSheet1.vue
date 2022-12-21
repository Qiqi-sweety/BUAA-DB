
<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="12"
        style = "padding-left: 25%;padding-top: 40px ;height: 140px">
          <n-statistic label="历史订单数量">
            {{ info.orders_num }}
          </n-statistic>
        </el-col>
      
        <el-col :span="12" 
        style="padding-left:15%;padding-top: 40px;">
          <n-statistic label="历史支出">
            ￥{{ info.total_money }}
          </n-statistic>
        </el-col>
    </el-row>
    <el-row>
      <el-col :span="12"><user-chart1 style="margin-left:100px"/></el-col>
      <el-col :span="12">
        <h3 style="30px">最常购买店铺：</h3>
        <h3 style="30px">{{info.favorite_store.name}}</h3>
        <img
        style="width:300px;height:300px;margin-left: 50px;"
        :src="`/api${info.favorite_store.logo}`"
         alt="暂无图片"/>
      </el-col>
    </el-row>
    <el-row>
      <n-button type="warning" style="margin-left:90%;margin-bottom:20px">导出图表</n-button>
    </el-row>
    <el-row>
      <user-chart2 style="background-color:white ; border-radius:20px" :month_info="info.month_info"/>
    </el-row>
    
</template>

<script setup>
import {NStatistic} from 'naive-ui'
import UserChart2 from "@/components/personalCenter/userChart2";
import UserChart1 from "@/components/personalCenter/userChart1";
import {onMounted, reactive} from "vue";
import {show_data} from "@/api/user";

const info = reactive({
  orders_num: 0,
  total_money: 0.0,
  favorite_store: {},
  month_info: {},
})

onMounted(() => {
  show_data().then(res => {
    let content = res.data
    console.log(content)
    if (res) {
      info.orders_num = content.orders_num
      info.total_money = content.total_money
      info.favorite_store = content.favorite_store
      info.month_info = content.month_info
    }
  })
})
  

</script>