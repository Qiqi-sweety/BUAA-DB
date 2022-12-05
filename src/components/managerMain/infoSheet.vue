<!-- managerMainPage的子组件：显示管理员可以看到的所有信息表 -->

<!-- TODO:
1.根据后端数据，导入所有的表格信息，并展示 -->

<template>
    <n-tabs type="segment">
    <n-tab-pane name="商家" tab="商家">
        <el-table :data="info.tableStore" style="width: 100%" table-layout="fixed">
            <el-table-column prop = "row_id" label="编号">
            </el-table-column>
            <el-table-column prop = "name" label="店铺名">
            </el-table-column>
            <el-table-column prop = "address" label="店铺地址">
            </el-table-column>

            
            <el-table-column label="logo">
                <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image :src="scope.row.店铺头像" style = "width: 80px;height: 80px;"/>
                </div>
                </template> 
            </el-table-column>
            <el-table-column prop = "店铺销量" label="店铺销量">
            </el-table-column>
        </el-table>
        
        
    </n-tab-pane>
    <n-tab-pane name="用户" tab="用户">
        <el-table :data="info.tableUser" stripe style="width: 100%" table-layout="fixed">
            <el-table-column prop = "row_id" label="编号" >
            </el-table-column>
            <el-table-column prop = "name" label="用户名">
            </el-table-column>
            <el-table-column prop = "address" label="用户地址">
            </el-table-column>

            <el-table-column prop = "银行卡号" label="银行卡号">
            </el-table-column>
            <el-table-column prop = "订单总量" label="订单总量">
            </el-table-column>

            <el-table-column label="用户头像">
<!--                <template #default="scope">-->
<!--                <div style="display: flex; align-items: center">-->
<!--                  <el-image :src="scope.row.用户头像" style = "width: 80px;height: 80px;"/>-->
                  <img src="../../assets/card.jpg" style = "width: 80px;height: 80px;"/>
<!--                </div>-->
<!--                </template> -->
            </el-table-column>
        </el-table>
       
    </n-tab-pane>
    <n-tab-pane name="订单" tab="订单">
        <el-table :data="info.tableOrder" style="width: 100%" table-layout="fixed">
            <el-table-column prop = "row_id" label="编号">
            </el-table-column>
            <el-table-column prop = "order_id" label="订单号">
            </el-table-column>
            <el-table-column prop = "store" label="店铺名">
            </el-table-column>

            <el-table-column prop = "user" label="购买者">
            </el-table-column>
            <el-table-column prop = "time" label="下单时间">
            </el-table-column>

            <el-table-column prop = "sum" label="金额">
            </el-table-column>

        </el-table>
       
    </n-tab-pane>

    <n-tab-pane name="评价" tab="评价">
        <el-table :data="info.tableComment" style="width: 100%" table-layout="fixed">
            <el-table-column prop = "row_id" label="编号">
            </el-table-column>
            <el-table-column prop = "order_id" label="订单号">
            </el-table-column>
            <el-table-column prop = "time" label="评价时间">
            </el-table-column>
            <el-table-column prop = "store_name" label="店铺名">
            </el-table-column>

            <el-table-column prop = "user_id" label="用户名">
            </el-table-column>


            <el-table-column prop = "star" label="星级">
            </el-table-column>

        </el-table>
       
    </n-tab-pane>


  </n-tabs>
</template>

<script setup>
import {NTabs, NTabPane} from "naive-ui"
import {onMounted, reactive} from "vue";
import {show_info} from "@/api/admin";

const info = reactive({
  tableStore: [],
  tableUser: [],
  tableOrder: [],
  tableComment: []
})

onMounted(() => {
  show_info({kind: "商家"}).then(res => {
    let content = res.data
    console.log(content)
    info.tableStore = []
    if (content.code === "200") {
      let i = 1
      content.list.forEach(item => {
        item.row_id = i
        i += 1
        info.tableStore.push(item)
      })
    }
  })
  show_info({kind: "用户"}).then(res => {
    let content = res.data
    console.log(content)
    info.tableUser = []
    if (content.code === "200") {
      let i = 1
      content.list.forEach(item => {
        item.row_id = i
        i += 1
        info.tableUser.push(item)
      })
    }
  })
  show_info({kind: "订单"}).then(res => {
    let content = res.data
    console.log(content)
    info.tableOrder = []
    if (content.code === "200") {
      let i = 1
      content.list.forEach(item => {
        item.row_id = i
        i += 1
        let sum = 0
        item.items.forEach(ii => {
          sum += ii.num * ii.item.price
        })
        item.sum = sum
        info.tableOrder.push(item)
      })
    }
  })
  show_info({kind: "评价"}).then(res => {
    let content = res.data
    console.log(content)
    info.tableComment = []
    if (content.code === "200") {
      let i = 1
      content.list.forEach(item => {
        item.row_id = i
        i += 1
        info.tableComment.push(item)
      })
    }
  })
})
</script>