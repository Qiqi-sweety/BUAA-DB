<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="12"
        style = "padding-left: 25%;padding-top: 40px ;height: 140px">
          <n-statistic label="用户总数">
        1,234,123
          </n-statistic>
        </el-col>
      
        <el-col :span="12" 
        style="padding-left:15%;padding-top: 40px;">
          <n-statistic label="店铺总数">
        1,234,123
          </n-statistic>
        </el-col>
        


        
    </el-row>

    <el-row style="margin-left:150px">

    <el-col :span="12">
        <h3 style="30px">历史销量最高店铺：</h3>
        <n-image
        style="width:300px;height:300px;margin-left: 50px;"
        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        />
      </el-col>

      <el-col :span="12">
        <h3 style="30px">评分最高店铺：</h3>
        <n-image
        style="width:300px;height:300px;margin-left: 50px;"
        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        />
      </el-col>

    </el-row>
    <el-row>
        <manageChart1 style="background-color:white;border-radius:20px;margin-top:50px"/>
    </el-row>

    <el-row>
        <manageChart2 style="background-color:white;border-radius:20px;margin-top:50px"/>
    </el-row>


    
    
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton,NStatistic,NImage} from 'naive-ui'
  import manageChart1 from './manageChart1.vue';
  import manageChart2 from './manageChart2.vue';

  export default defineComponent({
    components: {
      NTag,
      NButton,
      NStatistic,
      NImage,
      manageChart1,
      manageChart2,
    },
  })

  

</script>