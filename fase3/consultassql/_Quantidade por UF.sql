SELECT  
  v.UF,
  b.valor AS desc_valor,
  b.descricao_valor,
  COUNT(1) AS qt
FROM 
  `quantum-device-443518-b1.pnad_covid.pnad_covid` v
JOIN 
  `quantum-device-443518-b1.pnad_covid.dominio` a 
  ON a.codigo = 'UF'
JOIN 
  `quantum-device-443518-b1.pnad_covid.valores` b 
  ON b.cod_tabela = a.codigo 
  AND CAST(b.valor AS INT64)  = v.UF
GROUP BY 
  v.UF, b.valor, b.descricao_valor;
