<!-- 不包含商品信息的店铺卡片 -->
<!-- 用于userMainPage中按照商品搜索的结果展示 -->
<template>
    <n-card hoverable class = "storeCardClass1" embedded>
        <el-row>
            <el-col :span="10">
                <img :src="`/api${storeLogoUrl}`" class = "storeCardImageClass1">
            </el-col>
            <el-col :span="14">
                <h3 class = "nameClass">
                    {{storeName}}
                </h3>
                <el-row>
                    <el-col :span="12">
                        <n-rate allow-half readonly :default-value="star" class = "rateClass">
                        
                        </n-rate> 
                    </el-col>
                    <el-col :span="12">
                        <p class = "numberClass">
                        销量：{{number}}
                        </p>
                    </el-col>
                </el-row>
                
                <n-button type="warning" class = "inButtonClass" size = "large">
                进入店铺
              </n-button> 
            
            </el-col>
            
        </el-row>
    </n-card>
  </template>

<script>
import { defineComponent ,ref } from 'vue'
import { NCarousel,NCard,NButton, NRate} from 'naive-ui'
export default defineComponent({
  name: 'storeCard1',
  components: {
    NCarousel,
    NCard,
    NButton,
    NRate,

  },
  props:{
      storeLogoUrl:{
        type:String
      },
      storeName:{
        type:String
      },
      time:{
        type:String
      },
      star:{
        type:Number
      },
      number:{
        type:Number
      },
    }
})
</script>

<style>
.storeCardClass1 {
    width: 550px;
    height: 240px;
    padding-left: 0%;
}

.storeCardImageClass1 {
    margin-left: 0%;
    width: 200px;
    height: 200px;
   
}

.nameClass {
    font-size: 25px;
    margin-top: 0%;
    
}

.numberClass {
    margin-top: 20px;
}

.rateClass {
    
    margin-top: 20px;
}

.inButtonClass {
    margin-left: 180px;
    
}

</style>