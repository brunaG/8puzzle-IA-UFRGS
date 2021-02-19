import sys
import time
import heapq

class Node(object):
	def __init__(self, estado, acao, custo, path):
		self.estado= estado
		self.acao=acao
		self.custo=custo
		self.move=[]
		self.path=path

	def __lt__(self, other):
		return self.custo < other.custo

	def fora_lugar(self,test):
		solucao="12345678_"
		return sum (test[i] != solucao[i] for i in range(9))	

	def sucessor(self):
		def swap(id_a, id_b, ):
				str_list=list(self.estado)
				str_list[id_a]=self.estado[id_b]
				str_list[id_b]=self.estado[id_a]
				return "".join(str_list)

				
		spc_pos=self.estado.find("_")
		pares=[]
		if(spc_pos>2):
		#cima
			pares.append(("cima", swap(spc_pos,spc_pos-3)))
		if(spc_pos!=2 and spc_pos!=5 and spc_pos!=8):
		#direita
			pares.append(("direita",swap(spc_pos,spc_pos+1)))
		if(spc_pos<6):
		#baixo
			pares.append(("baixo",swap(spc_pos,spc_pos+3)))
		if(spc_pos!=0 and spc_pos!=3 and spc_pos!=6):
		#Esquerda
			pares.append(("esquerda",swap(spc_pos,spc_pos-1)))
		return pares


	def A_com_h1(self):
		explorados = []
		fronteira = []
		heapq.heappush(fronteira, (self.custo,self))
		final = self.estado
		while(len(fronteira)!=0):
			buff = heapq.heappop(fronteira)[1]
			final = buff.estado
			if(buff.fora_lugar(buff.estado) == 0):
				return final
			if(buff.estado not in explorados):
				explorados.append(buff.estado)
				sucessores = buff.sucessor()
				for suc_node in sucessores:
					h = self.fora_lugar(suc_node[1])
					v = Node(suc_node[1],suc_node[0],buff.custo+h+1,buff.path+[suc_node[0]])
					heapq.heappush(fronteira, (buff.custo+h+1, v))
		


def inicia(estado_ini):
	return Node(estado_ini, None, 0, [])

