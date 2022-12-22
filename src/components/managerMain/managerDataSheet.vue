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
      <n-button type="warning"
                style="margin-left:90%;margin-top:10px"
                @click="export_pic('1')"
      >导出图表</n-button>
    </el-row>

    <el-row>
        <manage-chart1
            :store_list="info.store_list"
            style="background-color:white;border-radius:20px;margin-top:10px"
        />
    </el-row>

    <el-row>
      <n-button type="warning"
                style="margin-left:90%;margin-top:30px"
                @click="export_pic('2')"
      >导出图表</n-button>
    </el-row>

    <el-row>
        <manage-chart2
            :unum="info.user_num"
            :snum="info.store_num"
            style="background-color:white;border-radius:20px;margin-top:10px"
        />
    </el-row>


    
    
    
</template>

<script setup>
import {NStatistic, NButton} from 'naive-ui'
import {onMounted, reactive} from "vue";
import {show_data} from "@/api/admin";
import ManageChart1 from "@/components/managerMain/manageChart1";
import ManageChart2 from "@/components/managerMain/manageChart2";

const info = reactive({
  store_num: 0,
  user_num: 0.0,
  best_sales_store: {},
  best_star_store: {},
  store_list: {s: [1, 1, 1, ]},
})

const echarts = require("echarts");
const export_pic = (id) => {
  let myChart = echarts.init(document.getElementById("manageChart" + id));
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
      info.store_num = content.store_num
      info.user_num = content.user_num
      info.best_sales_store = content.best_sales_store
      info.best_star_store = content.best_star_store
      info.store_list.s = []
      content.store_list.forEach(item => {
        info.store_list.s.push(item)
      })
    }
  })
})
</script>