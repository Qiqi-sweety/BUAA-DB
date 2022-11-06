<template>
    <n-card  style="margin-bottom: 50px"  class = "orderSheetCardClass">
        <el-row>
            <el-col :span="14"><h3 class = "orderId">订单号：{{orderId}}</h3></el-col>
            <el-col :span="10"><p class = "orderTime">日期：{{orderTime}}</p></el-col>
        </el-row>
        
        <!-- <h3 class = "orderTime">下单时间：2022.10.19</h3> -->
        <el-divider class = "orderDivider"/>

        <n-scrollbar class = "orderScrollbar">
            <orderSheetFoodCard/>
            <orderSheetFoodCard/>
            <orderSheetFoodCard/>
            <orderSheetFoodCard/>
            <orderSheetFoodCard/>
        </n-scrollbar>

        <el-row>
            <el-col :span="12"><h3>合计：{{money}}</h3></el-col>
            <el-col :span="12">
               
            </el-col>
        </el-row>
        
    </n-card>
    
   
</template>



<script>
  import { defineComponent ,ref } from 'vue'
  import {NButton,NCard,NScrollbar,NModal,NRate,NInput,NUpload} from 'naive-ui'
  import orderSheetFoodCard from '../cards/orderSheetFoodCard.vue'

  export default defineComponent({
    components: {
      NButton,
      NCard,
      NScrollbar,
      NModal,
      NRate,
      NInput,
      NUpload,
      orderSheetFoodCard,
    },
    props:{
        orderId:{
            type:String
        },
        orderTime:{
            type:String
        },
        money:{
            type:Number
        }
    },

    setup() {
    return {
      showModal: ref(false),
      value: ref(null)
    };
  }
  })

  


  </script>

<style>

.orderSheetCardClass {
    width: 320px;
    height: 400px;
    background-color: white;

}

.orderId {
    margin-top: 0%;
    margin-bottom: 0%;
}

.orderStoreName {
    font-size: 20px;
    margin-top: 0%;
    margin-bottom: 0%;
}
.orderDivider {
    margin-top: 0%;
}
.orderTime {
    margin-top: 2px;
    margin-bottom: 0%;
}

.orderScrollbar {
    margin-top: 0%;
    height: 230px;
    width: 280px;
    /* border: 2px solid palevioletred; */
}
.orderModelName {
    margin-top: 0%;
    font-size: 25px;
}

.orderModelTotal {
    margin-top: 0%;
    font-size:20px;
    /* border: 2px solid black;; */
}

.orderModelStar {
    margin-top: 2px;
    height: 50px;
    margin-bottom: 0%;
}

.orderModelText {
    margin-top: 0%;
    height: 150px;
}


</style>

