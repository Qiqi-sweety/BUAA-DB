<!-- managerMainPage的子组件：显示管理员可以看到的所有信息表 -->

<!-- TODO:
1.根据后端数据，导入所有的表格信息，并展示 -->

<template>
    <n-tabs type="segment">
    <n-tab-pane name="商家" tab="商家">
        <el-table :data="tableData1" style="width: 100%">
            <el-table-column prop = "编号" label="编号" width="200">
            </el-table-column>
            <el-table-column prop = "店铺名" label="店铺名" width="300">
            </el-table-column>
            <el-table-column prop = "店铺地址" label="店铺地址" width="400">
            </el-table-column>

            
            <el-table-column label="店铺头像" width="300">   
                <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image :src="scope.row.店铺头像" style = "width: 80px;height: 80px;"/>
                </div>
                </template> 
            </el-table-column>
            <el-table-column prop = "店铺销量" label="店铺销量" width="250">
            </el-table-column>
        </el-table>
        
        
    </n-tab-pane>
    <n-tab-pane name="用户" tab="用户">
        <el-table :data="tableData2" style="width: 100%">
            <el-table-column prop = "编号" label="编号" width="200">
            </el-table-column>
            <el-table-column prop = "用户名" label="用户名" width="250">
            </el-table-column>
            <el-table-column prop = "用户地址" label="用户地址" width="250">
            </el-table-column>

            <el-table-column prop = "银行卡号" label="银行卡号" width="250">
            </el-table-column>
            <el-table-column prop = "订单总量" label="订单总量" width="250">
            </el-table-column>

            <el-table-column label="用户头像" width="250">   
                <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image :src="scope.row.用户头像" style = "width: 80px;height: 80px;"/>
                </div>
                </template> 
            </el-table-column>
        </el-table>
       
    </n-tab-pane>
    <n-tab-pane name="订单" tab="订单">
        <el-table :data="tableData3" style="width: 100%">
            <el-table-column prop = "编号" label="编号" width="200">
            </el-table-column>
            <el-table-column prop = "订单号" label="订单号" width="300">
            </el-table-column>
            <el-table-column prop = "店铺名" label="店铺名" width="250">
            </el-table-column>

            <el-table-column prop = "购买者用户名" label="购买者用户名" width="250">
            </el-table-column>
            <el-table-column prop = "下单时间" label="下单时间" width="250">
            </el-table-column>

            <el-table-column prop = "金额" label="金额" width="200">
            </el-table-column>

        </el-table>
       
    </n-tab-pane>

    <n-tab-pane name="评价" tab="评价">
        <el-table :data="tableData4" style="width: 100%">
            <el-table-column prop = "编号" label="编号" width="200">
            </el-table-column>
            <el-table-column prop = "订单号" label="订单号" width="250">
            </el-table-column>
            <el-table-column prop = "评价时间" label="评价时间" width="250">
            </el-table-column>
            <el-table-column prop = "店铺名" label="店铺名" width="250">
            </el-table-column>

            <el-table-column prop = "用户名" label="用户名" width="250">
            </el-table-column>


            <el-table-column prop = "星级" label="星级" width="250">
            </el-table-column>

        </el-table>
       
    </n-tab-pane>


  </n-tabs>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NCard,NRate,NTabs,NTabPane} from 'naive-ui'

  export default defineComponent({
    components: {
      NCard,
      NRate,
      NTabPane,
      NTabs,
     
    },
    setup() {
      return {
        tableData1 :[
        {
          编号: 1,
          店铺名:"喜茶",
          店铺地址:"北京市海淀区学院路37号",
          店铺头像:require("@/assets/喜茶.jpg"),
          店铺销量: 100,
        },
        {
          编号: 2,
          店铺名:"喜茶",
          店铺地址:"北京市海淀区学院路37号",
          店铺头像:require("@/assets/喜茶.jpg"),
          店铺销量: 100,
        },
      
      ],
      tableData2 :[
        {
          编号: 1,
          用户名:"用户123456",
          用户头像:require("@/assets/logo.png"),
          用户地址:"北京市海淀区学院路37号",
          银行卡号:"0000 0000 0000 0000",
          订单总量: 100,
        },
        {
          编号: 2,
          用户名:"用户123456",
          用户头像:require("@/assets/logo.png"),
          用户地址:"北京市海淀区学院路37号",
          银行卡号:"0000 0000 0000 0000",
          订单总量: 100,
        },
      
      ],
      tableData3 :[
        {
          编号: 1,
          订单号: 12345678,
          店铺名: "喜茶",
          购买者用户名: "用户123456",
          下单时间: "2022.10.20",
          金额:19
        },
        {
          编号: 1,
          订单号: 12345678,
          店铺名: "喜茶",
          购买者用户名: "用户123456",
          下单时间: "2022.10.20",
          金额:19
        },
      
      ],
      tableData4 :[
        {
          编号: 1,
          订单号: 12345678,
          评价时间: "2022.10.20",
          店铺名: "喜茶",
          用户名: "用户123456",
          星级:4.5
        },
        {
          编号: 2,
          订单号: 12345678,
          评价时间: "2022.10.22",
          店铺名: "喜茶",
          用户名: "用户123456",
          星级:4
        },
      
      ]

      }
    }
  })
</script>