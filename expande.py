import sys
import time

class Node(object):
	def __init__(self, estado, acao, custo, path):
		self.estado= estado
		self.acao=acao
		self.custo=custo
		self.move=[]
		self.path=path
	
	def add_move(self, new_node):
		self.move.append(new_node)

	def __str__(self):
		return (str(self.estado)+"," +str(self.acao)+","+str(self.custo))
		
	def fora_lugar(self):
		solucao="12345678_"
		return sum (self.estado[i] != solucao[i] for i in range(9))	

	def imprimeFilhos(self):
		print(str(self))
		for m in self.move:
			print("("+str(m)+")",end="")
		print("")
	
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
			pares.append(("cima",swap(spc_pos,spc_pos-3)))
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


	def expande(self):
		sucessores=self.sucessor()
		for suc_node in sucessores:
			self.add_move(Node(suc_node[1],suc_node[0],self.custo+1, self.path+[suc_node[0]]))



def inicia(estado_ini):
	return Node(estado_ini, None, 0, [])



if __name__ == "__main__":
