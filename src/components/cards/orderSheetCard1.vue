<template>
    <n-card  style="margin-bottom: 50px"  class = "orderSheetCardClass">
        <el-row>
            <el-col :span="14"><h3 class = "orderId">订单号：{{orderId}}</h3></el-col>
            <el-col :span="10"><p class = "orderTime">日期：{{orderTime}}</p></el-col>
        </el-row>
        <h3 class = "orderStoreName">{{orderStoreName}}</h3>
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
                <n-button round type="warning" class = "orderRateButton" @click="showModal = true">
                评价
                </n-button>
            </el-col>
        </el-row>
        
    </n-card>
    <n-modal
    v-model:show="showModal"
    class="custom-card"
    preset="card"
    :style="bodyStyle"
    title="发表评价"
    style="width:850px;height:600px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 800px;height:500px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
            <h3 class = "orderModelName">{{orderStoreName}}</h3>
            <el-row>
                <el-col :span="3"><p class = "orderModelTotal">总体</p></el-col>
                <el-col :span="21"><n-rate allow-half size = "large" class = "orderModelStar"/></el-col>
            </el-row>
            <n-input
            v-model:value="value"
            type="textarea"
            placeholder="说说味道怎么样，给大家参考"
            class = "orderModelText"
            />

            <n-upload
            action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
            @before-upload="beforeUpload"
            style = "margin-top: 20px;"
            >
            <n-button>
                <template #icon>
                    <el-icon><Camera /></el-icon>
                </template>
                上传图片
            </n-button>
            </n-upload>
      <template #footer>
        <n-button style = "margin-left:320px;width: 100px;" size = "large" round type="warning">
        提交
        </n-button>
      </template>
    </n-card>
  </n-modal>

   
</template>



<script>
  import { defineComponent ,ref } from 'vue'
  import {NButton,NCard,NScrollbar,NModal,NRate,NInput,NUpload} from 'naive-ui'
  import orderSheetFoodCard from './orderSheetFoodCard.vue'

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
        orderStoreName:{
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
    height: 180px;
    width: 280px;
    /* border: 2px solid palevioletred; */
}

.orderRateButton {
    margin-left:50px;
    margin-top: 15px;
    width: 80px;
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