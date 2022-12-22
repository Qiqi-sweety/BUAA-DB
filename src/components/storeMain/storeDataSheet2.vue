<template>
  <el-row>
      <n-button type="warning" style="margin-left:90%;margin-bottom:20px" @click="export_table('tab1', '订单明细.xlsx')">导出为Excel</n-button>
  </el-row>
  <el-row>
    <el-table :data="tableData" style="width: 100%" id="tab1">
        <el-table-column prop="No" label="序号" width="180" />
        <el-table-column prop="date" label="订单日期" width="250" />
        <el-table-column prop="user" label="购买用户" width="250"/>
        <el-table-column prop="objects" label="商品内容" width="400"/>
        <el-table-column prop="money" label="总价" />
        <el-table-column prop="rate" label="评分" />
    </el-table>
  </el-row>
</template>

<script setup>
import {NButton} from 'naive-ui'
import FileSaver from 'file-saver'
import XLSX from 'xlsx'

const tableData = [
  {No: 1, date: '2022.12.22', user: 'lcm', objects: '冰糖葫芦(￥8)×2', money: 16, rate: 5}
]

const export_table = (id, filename) => {
  let wb = XLSX.utils.table_to_book(document.querySelector('#' + id), {
    raw: true // 如果表格里有数字、日期这些、需要加上raw: true
  });
  /* 获取二进制字符串作为输出 */
  let wbout = XLSX.write(wb, {
    bookType: 'xlsx',
    bookSST: true,
    type: 'array'
  });
  try {
    FileSaver.saveAs(
        // Blob 对象表示一个不可变、原始数据的类文件对象。
        new Blob([wbout], { type: 'application/octet-stream' }),
        // 设置导出文件名称
        filename
    );
  } catch (e) {
    if (typeof console !== 'undefined') console.log(e, wbout);
  }
  return wbout
}


</script>