<!-- 位于orderTabs评价卡 -->
<template>
    <NCard style = "width: 700px;height: 450px;" embedded>
        <el-row>
            <el-col :span="6">
                <img :src="{userLogoUrl}" 
                style = "width: 100px;height: 100px;border-radius: 20px;background-color: white;">
            </el-col>
            <el-col :span="14">
                <h3 style = "font-size: 25px;margin-bottom: 10px;">
                  {{userName}}
                </h3>
            </el-col>
            <el-col :span="4">
                <p style = "margin-top: 20px;color: gray;">
                  日期：{{time}}
                </p>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="14">
                <n-rate allow-half readonly :default-value="3.5" style = "margin-left: 20px;" size = "large">        
                </n-rate>
                <h3 style = "font-size: 17px;margin-left: 20px;margin-right: 20px;">
                  {{rateDetail}}
                  </h3>
            </el-col>
            <el-col :span="10">
              <img :src="{rateLogoUrl}" style = "margin-top: 0%;width: 240px;height: 290px;">
            </el-col>
        </el-row>
    </NCard>
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import {NCard,NRate} from 'naive-ui'

  export default defineComponent({
    components: {
      NCard,
      NRate,
    },
    props:{
      userLogoUrl:{
        type:String
      },
      userName:{
        type:String
      },
      time:{
        type:String
      },
      rateDetail:{
        type:String
      },
      rateLogoUrl:{
        type:String
      }
    }
  })
  </script>
