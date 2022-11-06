<template>
    <el-row class = "orderSheetFoodCardRow">
        <el-col :span="7">
            <img :src="{logoUrl}" class = "orderSheetfoodCardImage">
        </el-col>
        <el-col :span="11">
            <h3 class = "orderSheetFoodName">{{name}}</h3>
            <p class = "orderSheetFoodNumber">×{{number}}</p>
        </el-col>
        <el-col :span="6">
            <h3 class = "orderSheetFoodPrice">￥{{price}}</h3>
        </el-col>
    </el-row>
</template>



<script>
  import { defineComponent ,ref } from 'vue'
  import {NButton,NCard} from 'naive-ui'

  export default defineComponent({
    components: {
      NButton,
      NCard,
    },
    props:{
    logoUrl:{
      type:String
    },
    name:{
      type:String
    },
    number:{
      type:Number
    },
    price:{
      type:Number
    }
  },
  })
  </script>

<style>

.orderSheetFoodCardRow {
    height: 80px;
    margin-top: 0%;
    /* border: 2px solid black; */
}

.orderSheetfoodCardImage {
    width: 70px;
    height: 70px;
    margin-left: 0%;
    margin-top: 0%;
    padding-left: 0%;
    /* border: 2px solid black; */
}

.orderSheetFoodName {
    margin-top: 0%;
    font-size: 15px;
    /* margin-bottom: 5px; */
}

.orderSheetFoodNumber {
    margin-top: 0%;
    color: grey;
}

.orderSheetFoodPrice {
    margin-top: 0%;
}


</style>