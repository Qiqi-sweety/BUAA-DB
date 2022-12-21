<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="12"
        style = "padding-left: 25%;padding-top: 40px ;height: 140px">
          <n-statistic label="用户总数">
            {{ info.user_num }}
          </n-statistic>
        </el-col>
      
        <el-col :span="12" 
        style="padding-left:15%;padding-top: 40px;">
          <n-statistic label="店铺总数">
            {{ info.store_num }}
          </n-statistic>
        </el-col>
        


        
    </el-row>

    <el-row style="margin-left:150px">

    <el-col :span="12">
        <h3 style="30px">历史销量最高店铺：</h3>
        <h3 style="30px">{{info.best_sales_store.name}}</h3>
        <img
        style="width:300px;height:300px;margin-left: 50px;"
        :src="`/api${info.best_sales_store.logo}`"
        />
      </el-col>

      <el-col :span="12">
        <h3 style="30px">评分最高店铺：</h3>
        <h3 style="30px">{{info.best_star_store.name}}</h3>
        <img
            style="width:300px;height:300px;margin-left: 50px;"
            :src="`/api${info.best_star_store.logo}`"
        />
      </el-col>

    </el-row>

    <el-row>
      <n-button type="warning" style="margin-left:90%;margin-top:10px">导出图表</n-button>
    </el-row>

    <el-row>
        <manage-chart1 style="background-color:white;border-radius:20px;margin-top:10px"/>
    </el-row>

    <el-row>
      <n-button type="warning" style="margin-left:90%;margin-top:30px">导出图表</n-button>
    </el-row>

    <el-row>
        <manage-chart2 style="background-color:white;border-radius:20px;margin-top:10px" :unum="info.user_num" :snum="info.store_num"/>
    </el-row>


    
    
    
</template>

<script setup>
import {NStatistic} from 'naive-ui'
import {onMounted, reactive} from "vue";
import {show_data} from "@/api/admin";
import ManageChart1 from "@/components/managerMain/manageChart1";
import ManageChart2 from "@/components/managerMain/manageChart2";

const info = reactive({
  store_num: 0,
  user_num: 0.0,
  best_sales_store: {},
  best_star_store: {},
  store_list: {}
})

onMounted(() => {
  show_data().then(res => {
    let content = res.data
    console.log(content)
    if (res) {
      info.store_num = content.store_num
      info.user_num = content.user_num
      info.best_sales_store = content.best_sales_store
      info.best_star_store = content.best_star_store
      info.store_list = content.store_list
    }
  })
})
</script>