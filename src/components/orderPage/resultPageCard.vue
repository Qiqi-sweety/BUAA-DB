<!-- userOrderPage的子组件：搜索框搜索店内商品的商品结果展示界面 -->

<!-- TODO:
根据从userOrderPage传进来的搜索结果list实例化foodCard1的list，并进行展示 -->

<template>
    <h3
    style = "margin-left: 50px;
    font-size: 25px;
    margin-top:20px;
    margin-bottom: 0px;">
        
        搜索结果</h3>
    <n-card 
    style = " height: 95%;
            width: 95%;
            margin: auto;
            margin-top:2%;
            margin-bottom: 50px">

  <el-row class = "foodRowClass">
    <el-col :span="6"><foodCard1/></el-col>
    <el-col :span="6"><foodCard1/></el-col>
    <el-col :span="6"><foodCard1/></el-col>
    <el-col :span="6"><foodCard1/></el-col>
  </el-row>
</n-card>
</template>

<script>
import { defineComponent ,ref } from 'vue'
import { NCard} from 'naive-ui'

export default defineComponent({
  components: {
    NCard,
  },
})
</script>
<style>

.foodRowClass {
  margin-left : 50px;
}

</style>