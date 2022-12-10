
<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="12"
        style = "padding-left: 25%;padding-top: 40px ;height: 140px">
          <n-statistic label="历史订单数量">
        1,234,123
          </n-statistic>
        </el-col>
      
        <el-col :span="12" 
        style="padding-left:15%;padding-top: 40px;">
          <n-statistic label="历史支出">
        1,234,123
          </n-statistic>
        </el-col>
    </el-row>
    <el-row>
      <el-col :span="12"><user-chart1 style="margin-left:100px"/></el-col>
      <el-col :span="12">
        <h3 style="30px">最常购买店铺：</h3>
        <n-image
        style="width:300px;height:300px;margin-left: 50px;"
        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        />
      </el-col>
    </el-row>
    
    <el-row>
      <user-chart2 style="background-color:white ; border-radius:20px"/>
    </el-row>
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton,NStatistic,NImage} from 'naive-ui'
  import userChart1 from './userChart1.vue'
  import userChart2 from './userChart2.vue'
  export default defineComponent({
    components: {
      NTag,
      NButton,
      NStatistic,
      NImage,
      userChart1,
      userChart2,
    },
  })

  

</script>