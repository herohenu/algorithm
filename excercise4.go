package main

import "fmt"

/*
@Time: 2018-12-07 17:04
@Desc: n >1

*/
type Node struct {
	Left  int
	Right int
}

var W []int
var sum int

//add (0,0) at head and tail , have no effect on result
var nodes = []Node{
	{Left: 0, Right: 0},
	{Left: 5, Right: 8},
	{Left: 4, Right: 2},
	{Left: 9, Right: 6},
	{Left: 7, Right: 7},
	{Left: 3, Right: 9},
	{Left: 11, Right: 10},
	{Left: 0, Right: 0},
}

func main() {
	nodeStateInit()
	sumMax := MoveNode(0, len(nodes)-1)
	fmt.Println("sum max is  :", sumMax)
	//sum()
}

//当前节点是第一个那么必须指定为0
//否则判断下一个 的cj 和上一个的cj比较
func MoveNode(begin, end int) int {
	if begin < 0 || end >= len(nodes) || begin >= end {
		return 0
	}

	mid := int((begin + end) / 2)

	if end-begin == 1 {
		sum = nodes[begin].Right * nodes[end].Left
		return sum
	}

	val1 := MoveNode(begin, mid) + MoveNode(mid, end)
	swap(mid)
	val2 := MoveNode(begin, mid) + MoveNode(mid, end)
	if val1 > val2 {
		swap(mid)
		sum = val1
	} else {
		sum = val2
	}

	return sum
}

//swap node at index i left and right
func swap(mid int) {
	if mid <= 0 || mid >= len(nodes) {
		return
	}

	tmp := nodes[mid].Left
	nodes[mid].Left = nodes[mid].Right
	nodes[mid].Right = tmp
	if nodes[mid].Left < nodes[mid].Right {
		W[mid] = 0
	} else {
		W[mid] = 1
	}
}

//init node status to W
func nodeStateInit() {
	for _, node := range nodes {
		if node.Left < node.Right {
			W = append(W, 0)
		} else {
			W = append(W, 1)
		}
	}
}
