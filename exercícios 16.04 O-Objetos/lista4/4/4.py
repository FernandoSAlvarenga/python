class AgendaTelefonica:
 
  def __init__(self):
    self._contatos = []

  def adicionar_contato(self, nome, telefone, email):
    novo_contato = {"nome": nome, "telefone": telefone, "email": email}
    self._contatos.append(novo_contato)
    print(f"Contato '{nome}' adicionado com sucesso à agenda!")

  def buscar_contato(self, nome_ou_telefone):
    contato_encontrado = None
    for contato in self._contatos:
      if contato["nome"].lower() == nome_ou_telefone.lower() or contato["telefone"] == nome_ou_telefone:
        contato_encontrado = contato
        break

    if contato_encontrado:
      print(f"\nContato encontrado:")
      print(f"Nome: {contato_encontrado['nome']}")
      print(f"Telefone: {contato_encontrado['telefone']}")
      print(f"Email: {contato_encontrado['email']}")
    else:
      print(f"Contato '{nome_ou_telefone}' não encontrado na agenda.")

  def remover_contato(self, nome_ou_telefone):
    contato_removido = False
    for index, contato in enumerate(self._contatos):
      if contato["nome"].lower() == nome_ou_telefone.lower() or contato["telefone"] == nome_ou_telefone:
        del self._contatos[index]
        contato_removido = True
        break

    if contato_removido:
      print(f"Contato '{nome_ou_telefone}' removido com sucesso da agenda!")
    else:
      print(f"Contato '{nome_ou_telefone}' não encontrado na agenda. Operação ignorada.")

  def mostrar_contatos(self):
    if self._contatos:
      print("\n**Contatos da Agenda:**")
      for index, contato in enumerate(self._contatos):
        print(f"{index + 1}. {contato['nome']}: {contato['telefone']} ({contato['email']})")
    else:
      print("A agenda telefônica está vazia.")

# Exemplo de uso
agenda = AgendaTelefonica()

agenda.mostrar_contatos()  
agenda.adicionar_contato("João Silva", "11 9999-9999", "joao@email.com")
agenda.adicionar_contato("Maria Oliveira", "12 3456-7890", "maria@email.com.br")
agenda.adicionar_contato("João Silva", "13 8888-8888", "joao@outroemail.com")  # Erro: contato já existe (nome)

agenda.mostrar_contatos()

agenda.buscar_contato("Maria Oliveira")
agenda.buscar_contato("12 3456-7890")
agenda.buscar_contato("João Silva Inexistente")  

agenda.remover_contato("João Silva")  
agenda.remover_contato("13 8888-8888")  
agenda.remover_contato("Contato Inexistente")  

agenda.mostrar_contatos()