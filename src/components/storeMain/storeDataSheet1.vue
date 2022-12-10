<template>
    <el-row class = "numberClass" 
    style=
    "width: 80%;margin-left: 9%;background-color: white;height: 150px;border-radius: 10px;">
        <el-col :span="8"
        style = "padding-left: 10%;padding-top: 40px ;height: 140px">
          <n-statistic label="历史订单数量">
        1,234,123
          </n-statistic>
        </el-col>
      
        <el-col :span="8" 
        style="padding-left:10%;padding-top: 40px;">
          <n-statistic label="平均评分">
        1,234,123
          </n-statistic>
        </el-col>
        <el-col :span="8" 
        style="padding-left:10%;padding-top: 40px;">
          <n-statistic label="历史收入">
        1,234,123
          </n-statistic>
        </el-col>


        
    </el-row>
    <el-row>
      <storeChart1 style="background-color:white;border-radius: 20px;margin-top: 20px;"/>
    </el-row>
    <el-row>
      <storeChart2 style="background-color:white;border-radius: 20px;margin-top: 20px;"/>
    </el-row>
    
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton,NStatistic,NImage} from 'naive-ui'
  import storeChart1 from './storeChart1.vue';
  import storeChart2 from './storeChart2.vue';

  export default defineComponent({
    components: {
      NTag,
      NButton,
      NStatistic,
      NImage,
      storeChart1,
      storeChart2,

    },
  })

  

</script>