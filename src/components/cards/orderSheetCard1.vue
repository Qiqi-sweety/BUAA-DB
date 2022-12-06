<template>
    <n-card  style="margin-bottom: 50px"  class = "orderSheetCardClass">
        <el-row>
            <el-col :span="14"><h3 class = "orderId">订单号：{{props.order.order_id}}</h3></el-col>
            <el-col :span="10"><p class = "orderTime">日期：{{props.order.time}}</p></el-col>
        </el-row>
        <h3 class = "orderStoreName">{{props.order.store}}</h3>
        <el-divider class = "orderDivider"/>

        <n-scrollbar class = "orderScrollbar">
            <div v-for="item in props.order.items">
              <orderSheetFoodCard :item="item.item" :num="item.num"/>
            </div>
        </n-scrollbar>

        <el-row>
            <el-col :span="12"><h3>合计：￥{{sum}}</h3></el-col>
            <el-col :span="12">
              <div v-if="form.isCommented">
                <n-button disabled round type="warning" class = "orderRateButton" @click="showModal = true">
                  已评价
                </n-button>
              </div>
              <div v-else>
                <n-button round type="warning" class = "orderRateButton" @click="showModal = true">
                  评价
                </n-button>
              </div>
            </el-col>
        </el-row>
        
    </n-card>
    <n-modal
      v-model:show="showModal"
      class="custom-card"
      preset="card"
      title="发表评价"
      style="width:850px;"
      :bordered="false"
    >
<!--    :style="bodyStyle"-->
<!--    :segmented="segmented"-->

        <n-card
          style="width: 800px;"
          :bordered="false"
          size="huge"
          role="dialog"
          aria-modal="true"
        >
            <h3 class = "orderModelName">{{props.order.store}}</h3>
            <el-row>
                <el-col :span="3"><p class = "orderModelTotal">总体</p></el-col>
                <el-col :span="21">
                  <n-rate size="large" class="orderModelStar" v-model:value="form.star"/>
                </el-col>
            </el-row>
            <n-input
                v-model:value="form.input"
                type="textarea"
                placeholder="说说味道怎么样，给大家参考"
                class = "orderModelText"
            />

            <el-upload
                action="/api/image/update/"
                list-type="picture-card"
                :show-file-list="false"
                :limit="1"
                :on-success="handlePhotoSuccess"
                style = "margin-top: 20px;"
            >
              <el-image v-if="form.photo" fit="contain" :src="`/api${form.photo}`" class="avatar" />
              <el-icon v-else><Camera /></el-icon>
<!--              <n-button>-->
<!--                  <template #icon>-->
<!--                      <el-icon><Camera /></el-icon>-->
<!--                  </template>-->
<!--                  上传图片-->
<!--              </n-button>-->
            </el-upload>
      <template #footer>
        <n-button style = "margin-left:320px;width: 100px;" size = "large" round type="warning" @click="submitComment">
        提交
        </n-button>
      </template>
    </n-card>
  </n-modal>

   
</template>



<script setup>
import {reactive, ref} from 'vue'
import {NButton,NCard,NScrollbar,NModal,NRate,NInput} from 'naive-ui'
import {write_comment} from "@/api/user";
import {ElMessage} from "element-plus";

const showModal = ref(false)
const form = reactive({
  input: '',
  star: 0,
  photo: '',
  isCommented: false, // todo: 临时变量名，具体看接口user/showOrders/
})
const props = defineProps({
  order: Object
})
const calSum = () => {
  let ans = 0
  props.order.items.forEach(item => {
    ans += item.item.price * item.num
  })
  return ans
}
const sum = ref(calSum())

const handlePhotoSuccess = (res) => {
  console.log(res)
  form.photo = res.url
}

const submitComment = () => {
  if (form.star === 0) {
    ElMessage({message: "请为本订单评星", type: "error"})
    return
  }
  write_comment({
    content: form.input,
    order_id: props.order.order_id,
    photo: form.photo,
    star: form.star
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
  })
  showModal.value = false
  form.isCommented = true
}

</script>

<style>

.orderSheetCardClass {
    width: 320px;
    height: 400px;
    background-color: white;

}

.orderId {
    margin-top: 0;
    margin-bottom: 0;
}

.orderStoreName {
    font-size: 20px;
    margin-top: 0;
    margin-bottom: 0;
}
.orderDivider {
    margin-top: 0;
}
.orderTime {
    margin-top: 2px;
    margin-bottom: 0;
}

.orderScrollbar {
    margin-top: 0;
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
    margin-top: 0;
    font-size: 25px;
}

.orderModelTotal {
    margin-top: 0;
    font-size:20px;
    /* border: 2px solid black;; */
}

.orderModelStar {
    margin-top: 2px;
    height: 50px;
    margin-bottom: 0;
}

.orderModelText {
    margin-top: 0;
    height: 150px;
}


</style>